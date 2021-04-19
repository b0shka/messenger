import os
import sys
import time
import json
import socket
import threading
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from style import main
from method.settings import Settings
from method.panel_user import Users
from method.send_message import message_monitor


class Client(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setIcon()

        self.ip = None
        self.port = None
        self.name = None
        self.number = None
        self.country = None
        self.connect_status = False
        self.all_users = []

        # Создание прототипа класса с отправкой, полученим и шифрованием всех сообщений
        self.connect_monitor = message_monitor()
        self.connect_monitor.mysignal.connect(self.signal_handler)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()

        self.connect_to_server()
        self.click_button()

    def setIcon(self):
    	self.appIcon = QIcon('style/icon.png')
    	self.setWindowIcon(self.appIcon)

    # Перетаскивание безрамочного окна
    # ==================================================================
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass
    # ==================================================================

    # Получение сообщений
    def signal_handler(self, value: list):
        if value[0] == 'update_config':
            self.update_config()
        else:
            message_time = str(time.strftime("%H:%M"))
            item = QtWidgets.QListWidgetItem()
            
            if value[0] == "SERVER_INFO":
                self.connect_status = True
                item.setTextAlignment(QtCore.Qt.AlignHCenter)
                item.setText(f'({message_time}) {value[1]}')
                self.listWidget.addItem(item)

            elif value[0] == "ENCRYPT_MESSAGE":
                item.setTextAlignment(QtCore.Qt.AlignLeft)
                item.setText(f"({message_time}) [{value[1]}] {value[-1]}")
                self.listWidget.addItem(item)

            elif value[0] == "SERVER_MESSAGE":
                item.setTextAlignment(QtCore.Qt.AlignHCenter)
                item.setText(f"({message_time}) {value[-1]}")
                self.listWidget.addItem(item)

            elif value[0] == 'LIST_USER':
                self.all_users = value[-1]

    # Функции для кнопок
    def click_button(self):
        self.pushButton.clicked.connect(self.write_message)
        self.pushButton_2.clicked.connect(self.setting_panel)
        self.pushButton_3.clicked.connect(self.users_panel)
        self.pushButton_4.clicked.connect(lambda: self.showMinimized())
        self.pushButton_5.clicked.connect(lambda: self.close())

        self.lineEdit.returnPressed.connect(self.write_message)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    # Соединение с сервером
    def connect_to_server(self):
        self.update_config()

        if self.name != None:
            try:
                self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client.connect((self.ip, self.port))
                self.connect_monitor.server_socket = self.client
                self.connect_monitor.start()

                payload = ['CONNECT_SERVER', self.name]
                self.connect_monitor.send_encrypt(payload)

            except Exception as e:
                print(e)
                message = "Ошибка соединения с сервером.\nПроверьте правильность ввода данных"
                QtWidgets.QMessageBox.about(self, "Оповещение", message)
        else:
            message = 'Для начала введите имя в настройках'
            QtWidgets.QMessageBox.about(self, "Оповещение", message)

    # Получение данных из файла
    def update_config(self):
        if os.path.exists(os.path.join("data", "config.json")):
            with open(os.path.join("data", "config.json")) as file:
                data = json.load(file)
                self.name = data['nick']
                self.number = data['number_phone']
                self.country = data['country']

        if os.path.exists(os.path.join("data", "data_server.json")):
            with open(os.path.join("data", "data_server.json")) as file:
                data = json.load(file)
                self.ip = data['server_ip']
                self.port = int(data['server_port'])

    # Написание и отправка сообщений на сервер другим пользователям
    def write_message(self):
        if self.connect_status:
            self.update_config()
            message = self.lineEdit.text()

            if len(message) > 0:
                if message.lower() == 'clear':
                    self.listWidget.clear()
                else:
                    payload = ['ENCRYPT_MESSAGE', self.name, message.encode()]
                    self.connect_monitor.send_encrypt(payload)

                    message_time = str(time.strftime("%H:%M"))
                    item = QtWidgets.QListWidgetItem()
                    item.setTextAlignment(QtCore.Qt.AlignRight)
                    item.setText(f'({message_time}) {message}')
                    self.listWidget.addItem(item)

                self.lineEdit.clear()

    # Открыть окно для настройки клиента
    def setting_panel(self):
        settings = Settings(self.client, self.connect_monitor.mysignal)
        settings.show()

    # Открыть окно с пользователями чата
    def users_panel(self):
        list_users = Users(self.all_users)
        list_users.show()

    '''def mousePressEvent(self, event):
        self.close()'''

    # При выходе из программы
    def closeEvent(self, value: QtGui.QCloseEvent) -> None:
        try:
            payload = ['EXIT', f'{self.name}', 'покинул чат'.encode()]
            self.connect_monitor.send_encrypt(payload)
            self.hide()
            time.sleep(2)
            self.client.close()
            self.close()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Client()
    window.show()
    sys.exit(app.exec_())