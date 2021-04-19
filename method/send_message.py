import time
import pickle
from random import randint
from PyQt5 import QtCore
from cryptography.fernet import Fernet


class message_monitor(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(list)
    server_socket = None
    symmetric_key = None

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        while True:
            if self.server_socket != None:
                try:
                    message = self.server_socket.recv(1024)
                    pickle_dec = pickle.loads(message)

                    if pickle_dec[0] == "SERVER_INFO":
                        self.symmetric_key = pickle_dec[-1]
                        self.cipher = Fernet(self.symmetric_key)
                        self.mysignal.emit(pickle_dec)

                    elif pickle_dec[0] == "ENCRYPT_MESSAGE":
                        decrypted_text = self.cipher.decrypt(pickle_dec[-1]).decode()
                        decrypted_payload = ["ENCRYPT_MESSAGE", pickle_dec[1], decrypted_text]
                        self.mysignal.emit(decrypted_payload)

                    elif pickle_dec[0] == "SERVER_MESSAGE":
                        payload = ["SERVER_MESSAGE", pickle_dec[-1]]
                        self.mysignal.emit(payload)

                    elif pickle_dec[0] == 'LIST_USER':
                        payload = ["LIST_USER", pickle_dec[-1]]
                        self.mysignal.emit(payload)
                except EOFError:
                    pass

            time.sleep(1)

    def send_encrypt(self, data_list):
        if data_list[0] == "ENCRYPT_MESSAGE":
            encrypted_message = self.cipher.encrypt(data_list[-1])
            pickle_payload = ['ENCRYPT_MESSAGE', data_list[1], encrypted_message]
            self.server_socket.send(pickle.dumps(pickle_payload))

        elif data_list[0] == 'CONNECT_SERVER':
            not_encrypt_message = ["CONNECT_SERVER", data_list[-1]]
            self.server_socket.send(pickle.dumps(not_encrypt_message))

        elif data_list[0] == 'CHANGE_NAME':
            not_encrypt_message = ["CHANGE_NAME", data_list[-1]]
            self.server_socket.send(pickle.dumps(not_encrypt_message))

        elif data_list[0] == "EXIT":
            pickle_payload = ['EXIT', data_list[1], data_list[-1]]
            self.server_socket.send(pickle.dumps(pickle_payload))