#!/usr/bin/python

from PyQt5 import QtGui, QtCore, QtWidgets
import threading
import IHM
import sys

class IHMViewer(QtWidgets.QMainWindow, IHM.Ui_IHM):
    def __init__(self, bluetooth_thread, commands):
        super(IHMViewer, self).__init__(None)
        self.setupUi(self, bluetooth_thread, commands)

    def main(self):
        self.show()


class graphical_thread():

    def handleValueUpdated(self, value, commands):
        self.mIHM.updateValue(value, commands)
        self.app.processEvents()

    def __init__(self, bluetooth_thread, commands):
        self.bluetooth_thread = bluetooth_thread
        self.commands = commands
        self.mIHM = None
        self.app = None

    def run(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.mIHM = IHMViewer(self.bluetooth_thread, self.commands)
        self.mIHM.main()
        self.app.exec_()