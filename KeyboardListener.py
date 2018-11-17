from builtins import str
from pynput.keyboard import Key, Listener
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from message_builder import message_builder

class KeyboardListener:

    def __init__(self, bluetooth_thread, commands, graphical_thread):
        self.commands = commands
        self.bluetooth_thread = bluetooth_thread
        self.graphical_thread = graphical_thread


    def on_key_release(self, key):
        self.graphical_thread.app.processEvents()
        if '{0}'.format(key) == "'z'":
            self.commands['up'] = 0
            self.graphical_thread.mIHM.pushButton.setDown(False)
        elif '{0}'.format(key) == "'s'":
            self.commands['down']= 0
            self.graphical_thread.mIHM.pushButton_4.setDown(False)
        elif '{0}'.format(key) == "'q'":
            self.commands['left'] = 0
            self.graphical_thread.mIHM.pushButton_2.setDown(False)
        elif '{0}'.format(key) == "'d'":
            self.commands['right']= 0
            self.graphical_thread.mIHM.pushButton_3.setDown(False)
        elif '{0}'.format(key) == "'p'":
            self.commands['arm_up'] = 0
            self.graphical_thread.mIHM.pushButton_6.setDown(False)
        elif '{0}'.format(key) == "'m'":
            self.commands['arm_down'] = 0
            self.graphical_thread.mIHM.pushButton_5.setDown(False)
        self.graphical_thread.app.processEvents()
        self.bluetooth_thread.message = message_builder(self.commands)

    def on_key_press(self, key):
        self.graphical_thread.app.processEvents()
        if '{0}'.format(key) == "'z'":
            self.commands['up'] = 1
            self.graphical_thread.mIHM.pushButton.setDown(True)
        elif '{0}'.format(key) == "'s'":
            self.commands['down']= 1
            self.graphical_thread.mIHM.pushButton_4.setDown(True)
        elif '{0}'.format(key) == "'q'":
            self.commands['left'] = 1
            self.graphical_thread.mIHM.pushButton_2.setDown(True)
        elif '{0}'.format(key) == "'d'":
            self.commands['right']= 1
            self.graphical_thread.mIHM.pushButton_3.setDown(True)
        elif '{0}'.format(key) == "'p'":
            self.commands['arm_up'] = 1
            self.graphical_thread.mIHM.pushButton_6.setDown(True)
        elif '{0}'.format(key) == "'m'":
            self.commands['arm_down'] = 1
            self.graphical_thread.mIHM.pushButton_5.setDown(True)
        self.graphical_thread.app.processEvents()
        self.bluetooth_thread.message = message_builder(self.commands)


    def run(self):
        with Listener(on_press= self.on_key_press, on_release= self.on_key_release) as listener:
            listener.join()