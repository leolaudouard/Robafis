from pynput.keyboard import Key, Listener
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import threading

class KeyboardListener(threading.Thread):

    def __init__(self, commands):
        threading.Thread.__init__(self)
        self.commands = commands
        self.updating = False


    def on_key_release(self, key):
        if '{0}'.format(key) == "'z'":
            self.commands['forward'] = 0

        elif '{0}'.format(key) == "'s'":
            self.commands['backward']= 0

        elif '{0}'.format(key) == "'q'":
            self.commands['left'] = 0

        elif '{0}'.format(key) == "'d'":
            self.commands['right']= 0

        elif '{0}'.format(key) == "'p'":
            self.commands['up'] = 0

        elif '{0}'.format(key) == "'m'":
            self.commands['down'] = 0

    def on_key_press(self, key):
        self.updating = True
        if '{0}'.format(key) == "'z'":
            self.commands['forward'] = 1

        elif '{0}'.format(key) == "'s'":
            self.commands['backward']= 1

        elif '{0}'.format(key) == "'q'":
            self.commands['left'] = 1

        elif '{0}'.format(key) == "'d'":
            self.commands['right']= 1

        elif '{0}'.format(key) == "'p'":
            self.commands['up'] = 1
        elif '{0}'.format(key) == "'m'":
            self.commands['down'] = 1


    def run(self):
        with Listener(on_press= self.on_key_press, on_release= self.on_key_release) as listener:
            listener.join()