import os
import re
import json
import time
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from style import settings_window
from method.send_message import message_monitor


class Settings(QtWidgets.QMainWindow, settings_window.Ui_Form):
    def __init__(self, client, signal=None):
        super().__init__()
        self.setupUi(self)

        self.signal = signal
        self.client = client
        self.ip = None
        self.port = None
        self.old_name = None

        self.connect_monitor = message_monitor()
        self.connect_monitor.server_socket = self.client

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()

        self.pushButton_7.clicked.connect(lambda: self.close())
        self.pushButton_6.clicked.connect(self.save_data)

        # Подгружаем настройки если они уже имеются
        if os.path.exists(os.path.join("data", "config.json")):
            with open(os.path.join("data", "config.json")) as file:
                data = json.load(file)
                self.lineEdit_1.setText(data['nick'])
                self.lineEdit_2.setText(data['number_phone'])
                self.lineEdit_3.setText(str(data['country']))
                self.old_name = data['nick']

        if os.path.exists(os.path.join("data", "data_server.json")):
            with open(os.path.join("data", "data_server.json")) as file:
                data = json.load(file)
                self.label.setText('IP -  ' + str(data['server_ip']))
                self.label_2.setText('PORT -  ' + str(data['server_port']))
                self.ip = data['server_ip']
                self.port = int(data['server_port'])

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

    # Сохранение данных
    def save_data(self):
        name = self.lineEdit_1.text()
        number = self.lineEdit_2.text()
        country = self.lineEdit_3.text()
        #regular_ip = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        #if not re.match(regular_ip, self.lineEdit_2.text()) is None:
        users_data = {"nick": name, "number_phone": number, "country": country}

        self.lineEdit_1.setStyleSheet("border-radius: 7px;")
        self.lineEdit_2.setStyleSheet("border-radius: 7px;")
        self.lineEdit_3.setStyleSheet("border-radius: 7px;")

        if len(name) >= 3 and len(name) <= 30:
            if len(number) != 0:
                if len(number) >= 11 and len(number) <= 16:
                    with open(os.path.join("data", "config.json"), 'w') as file:
                        json.dump(users_data, file, indent=2)

                    self.close()
                else:
                    self.lineEdit_2.setStyleSheet("border: 2px solid red; border-radius: 7px;")
            else:
                with open(os.path.join("data", "config.json"), 'w') as file:
                    json.dump(users_data, file, indent=2)

                self.close()
                self.signal.emit(['update_config'])
                
        else:
            self.lineEdit_1.setStyleSheet("border: 2px solid red; border-radius: 7px;")

        if name != self.old_name:
            payload = ['CHANGE_NAME', f'{self.old_name},{name}']
            self.connect_monitor.send_encrypt(payload)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Settings()
    window.show()
    sys.exit(app.exec_())