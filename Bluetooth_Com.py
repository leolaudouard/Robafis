import threading
from bluetooth import *
import time


class bluetooth_thread(threading.Thread):

    def __init__(self, mac_adress, message):
        threading.Thread.__init__(self)
        self.client_socket = BluetoothSocket(RFCOMM)
        self.mac_adress = mac_adress
        self.message = message

    def set_message(self, message):
        self.message = message

    def run(self):

        while True:
            self.client_socket.connect((self.mac_adress, 3))

            try:
                while True:
                    time.sleep(1)
                    self.client_socket.send(self.message)
                    print("Send : " + self.message)
                    data = self.client_socket.recv(4)
                    if len(data) == 0: break
                    print ("received [%s]" %data)
            except IOError:
                pass
            self.client_socket.close()
