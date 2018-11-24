import threading
from bluetooth import *
import time
import math
from message_builder import message_builder

class bluetooth_thread(threading.Thread):

    def __init__(self, mac_adress, message):
        threading.Thread.__init__(self)
        self.client_socket = BluetoothSocket(RFCOMM)
        self.mac_adress = mac_adress
        self.message = message
        self.speed = 0
        self.motor_speed = 0
        self.connected = False
        self.limit = 80


    def set_params(self, graphical_thread, KeyboardListener):
        self.graphical_thread = graphical_thread
        self.KeyboardListener = KeyboardListener

    def run(self):

        while True:
            print ("Trying to connect to I'ROBOT")
            self.client_socket = BluetoothSocket(RFCOMM)
            try:
                self.client_socket.connect((self.mac_adress, 3))
                self.connected = True
                if self.graphical_thread.mIHM != None:
                    self.graphical_thread.handleValueUpdated(0, self.KeyboardListener.commands, False, self.connected)
            except IOError:
                print ("Failed to connect to I'ROBOT")
                self.connected = False
                time.sleep(1)

            self.connected = True
            if self.connected:
                try:
                    while True:

                        self.motor_speed = self.client_socket.recv(10).decode('utf-8')
                        self.speed = math.fabs(int(self.motor_speed)*2*math.pi*30/(2*60*7.26))     #calculer la vitesse

                        self.message = message_builder(self.KeyboardListener.commands)
                        if self.graphical_thread.mIHM != None:
                            if self.graphical_thread.mIHM.tabWidget.currentIndex() == 0:
                                self.message = self.message[0:5] + '00' + self.message[7]

                        self.client_socket.send(self.message.encode('utf-8'))
                        print (self.message)
                        if self.message[7] == 1:
                            self.limit = 80
                        else:
                            self.limit = 15
                        if (self.graphical_thread.mIHM != None):
                            self.graphical_thread.handleValueUpdated(self.speed, self.KeyboardListener.commands, self.speed > self.limit, self.connected)
                        time.sleep(0.02)
                except IOError:
                    pass
                print ("Disconnected")
                self.client_socket.close()
                self.connected = False
                self.graphical_thread.handleValueUpdated(0, self.KeyboardListener.commands, False, self.connected)
                time.sleep(1)
