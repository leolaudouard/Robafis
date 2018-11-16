#!/usr/bin/python

from PyQt5 import QtGui, QtCore, QtWidgets
import threading
import IHM
import sys

class IHMViewer(QtWidgets.QMainWindow, IHM.Ui_IHM):
    def __init__(self, bluetooth_thread):
        super(IHMViewer, self).__init__(None)
        self.setupUi(self)
        self.bluetooth_thread = bluetooth_thread

    def main(self):
        self.show()


class graphical_thread(threading.Thread):

    def __init__(self, bluetooth_thread):
        threading.Thread.__init__(self)
        self.bluetooth_thread = bluetooth_thread

    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        mIHM = IHMViewer(self.bluetooth_thread)
        mIHM.main()
        app.exec_()




    def released(self, key):
        # TODO : find a way to press graphical buttons
        if key == 'upp':
            print('up')


    def pressed(self, key):
        #TODO : find a way to press graphical buttons
        if key == 'upp':
            print ('up')