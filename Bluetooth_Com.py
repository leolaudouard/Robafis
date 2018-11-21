import threading
from bluetooth import *
import time
import math

class bluetooth_thread(threading.Thread):

    def __init__(self, mac_adress, message):
        threading.Thread.__init__(self)
        self.client_socket = BluetoothSocket(RFCOMM)
        self.mac_adress = mac_adress
        self.message = message
        self.speed = 0
        self.data = {'motor_1': 0,
                     'motor_2': 0}
    def set_graph_param(self, graphical_thread):
        self.graphical_thread = graphical_thread

    def run(self):

        while True:
            self.client_socket.connect((self.mac_adress, 3))

            try:
                while True:
                    self.data['motor_1'] = int(ord(self.client_socket.recv(1)))
                    self.data['motor_2'] = int(ord(self.client_socket.recv(1)))
                    # if len(data) == 0: break
                    # print (self.data['motor_1'])
                    # print (self.data['motor_2'])
                    self.speed = (self.data['motor_1'] + self.data['motor_2'])*2*math.pi*30/(2*60*7.26)
                    # print (self.speed)
                    self.client_socket.send(self.message.encode('utf-8'))
                    # print("Send : " + self.message)
                    if self.graphical_thread.mIHM != '':
                        self.graphical_thread.mIHM.progressBar.setProperty("value", self.speed)
                        self.graphical_thread.mIHM.progressBar_2.setProperty("value", self.speed)
            except IOError:
                pass
            print ("Disconnected")
            self.client_socket.close()
