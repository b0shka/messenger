import time
import json
import socket
import threading
import logging
import pickle
from cryptography.fernet import Fernet

logging.basicConfig(filename="info.log", format = u'[%(levelname)s] %(asctime)s: %(message)s', level='INFO')
global logger
logger = logging.getLogger()


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.all_client = []
        self.all_username = []
        self.symmetric_key = None

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.server.bind((self.ip, self.port))
        except OSError as e:
            print('Error port')
            logger.error(f'Error port, {e}')
        self.server.listen(0)
        threading.Thread(target=self.connect_handler).start()
        print('Server started')
        logger.info('Server started')

    # Подключение в серверу
    def connect_handler(self):
        while True:
            client, address = self.server.accept()
            if client not in self.all_client:
                self.all_client.append(client)

                self.get_key()

                payload = ['SERVER_INFO', 'Успешное подключение к чату', self.symmetric_key]
                client.send(pickle.dumps(payload))
                print(f'{address} - connect the chat')
                logger.info(f'{address} - connect the chat')
                threading.Thread(target=self.message_handler, args=(client,)).start()

            time.sleep(2)

    # Получение сообщений от пользователей
    def message_handler(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024)
                if len(message) > 0:
                    pickle_dec = pickle.loads(message)
            except:
                self.all_client.remove(client_socket)
                break

            try:
                # Простая отправка сообщения
                if pickle_dec[0] == "ENCRYPT_MESSAGE":
                    for i in self.all_client:
                        if i != client_socket:
                            i.send(message)

                # При добавлении нового пользователя
                elif pickle_dec[0] == "CONNECT_SERVER":
                    self.all_username.append(pickle_dec[-1])
                    for i in self.all_client:
                        if i != client_socket:
                            payload = ['SERVER_MESSAGE', f'{pickle_dec[-1]} подключился к чату']
                            i.send(pickle.dumps(payload))
                    time.sleep(1)
                    for i in self.all_client:
                        payload = ['LIST_USER', self.all_username]
                        i.send(pickle.dumps(payload))

                # При смене имени
                elif pickle_dec[0] == 'CHANGE_NAME':
                    names = pickle_dec[-1].split(',')
                    print(names)
                    self.all_username.remove(names[0])
                    self.all_username.append(names[1])
                    print(self.all_username)
                    for i in self.all_client:
                        payload = ['LIST_USER', self.all_username]
                        i.send(pickle.dumps(payload))

                # При выходе из программы
                elif pickle_dec[0] == "EXIT":
                    self.all_client.remove(client_socket)
                    self.all_username.remove(pickle_dec[1])
                    print(f'{str(client_socket).split("raddr=")[-1][:-1]} - leave the chat')
                    logger.info(f'{str(client_socket).split("raddr=")[-1][:-1]} - leave the chat')
                    for i in self.all_client:
                        if i != client_socket:
                            payload = ['SERVER_MESSAGE', f'{pickle_dec[1]} покинул чат']
                            i.send(pickle.dumps(payload))
                    for i in self.all_client:
                        payload = ['LIST_USER', self.all_username]
                        i.send(pickle.dumps(payload))
                    break

                time.sleep(1)
            except Exception as e:
                print(f'Error, {e}')
                logger.error(f'Error get message, {e}')

    # Генерация ключа шифрования
    def get_key(self) -> None:
        if self.symmetric_key is None:
            self.symmetric_key = Fernet.generate_key()


if __name__ == "__main__":
    myserver = Server('127.0.0.1', 9009)
