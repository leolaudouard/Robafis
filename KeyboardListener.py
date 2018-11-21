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
        tab_index = self.graphical_thread.mIHM.tabWidget.currentIndex()
        self.graphical_thread.app.processEvents()
        if '{0}'.format(key) == "'z'":
            self.commands['forward'] = 0
            self.graphical_thread.mIHM.forward.setDown(False)
            self.graphical_thread.mIHM.forward_2.setDown(False)

        elif '{0}'.format(key) == "'s'":
            self.commands['backward']= 0
            self.graphical_thread.mIHM.backward.setDown(False)
            self.graphical_thread.mIHM.backward_2.setDown(False)

        elif '{0}'.format(key) == "'q'":
            self.commands['left'] = 0
            self.graphical_thread.mIHM.left.setDown(False)
            self.graphical_thread.mIHM.left_2.setDown(False)

        elif '{0}'.format(key) == "'d'":
            self.commands['right']= 0
            self.graphical_thread.mIHM.right.setDown(False)
            self.graphical_thread.mIHM.right_2.setDown(False)

        elif '{0}'.format(key) == "'p'":
            if tab_index == 1 :
                self.commands['up'] = 0
                self.graphical_thread.mIHM.up.setDown(False)

        elif '{0}'.format(key) == "'m'":
            if tab_index == 1:
                self.commands['down'] = 0
                self.graphical_thread.mIHM.down.setDown(False)

        self.graphical_thread.app.processEvents()
        self.bluetooth_thread.message = message_builder(self.commands)

    def on_key_press(self, key):
        tab_index = self.graphical_thread.mIHM.tabWidget.currentIndex()
        self.graphical_thread.app.processEvents()
        if '{0}'.format(key) == "'z'":
            self.commands['forward'] = 1
            self.graphical_thread.mIHM.forward.setDown(True)
            self.graphical_thread.mIHM.forward_2.setDown(True)

        elif '{0}'.format(key) == "'s'":
            self.commands['backward']= 1
            self.graphical_thread.mIHM.backward.setDown(True)
            self.graphical_thread.mIHM.backward_2.setDown(True)

        elif '{0}'.format(key) == "'q'":
            self.commands['left'] = 1
            self.graphical_thread.mIHM.left.setDown(True)
            self.graphical_thread.mIHM.left_2.setDown(True)

        elif '{0}'.format(key) == "'d'":
            self.commands['right']= 1
            self.graphical_thread.mIHM.right.setDown(True)
            self.graphical_thread.mIHM.right_2.setDown(True)

        elif '{0}'.format(key) == "'p'":
            if tab_index == 1:
                self.commands['up'] = 1
                self.graphical_thread.mIHM.up.setDown(True)
        elif '{0}'.format(key) == "'m'":
            if tab_index == 1:
                self.commands['down'] = 1
                self.graphical_thread.mIHM.down.setDown(True)
        self.graphical_thread.app.processEvents()
        self.bluetooth_thread.message = message_builder(self.commands)


    def run(self):
        with Listener(on_press= self.on_key_press, on_release= self.on_key_release) as listener:
            listener.join()