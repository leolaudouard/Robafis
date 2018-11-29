#!/usr/bin/python

from PyQt5 import QtGui, QtCore, QtWidgets
import IHM
import sys

class IHMViewer(QtWidgets.QMainWindow, IHM.Ui_IHM):
    def __init__(self, commands):
        super(IHMViewer, self).__init__(None)
        self.setupUi(self, commands)

    def main(self):
        self.show()


class graphical_thread():

    def handleValueUpdated(self, value, commands, speed_limit,connection, lineFollower):
        self.mIHM.updateValue(value, commands, speed_limit, connection, lineFollower)
        self.app.processEvents()

    def __init__(self, commands):
        self.commands = commands
        self.mIHM = None
        self.app = None

    def run(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.mIHM = IHMViewer(self.commands)
        self.mIHM.main()
        self.app.exec_()