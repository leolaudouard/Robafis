#!/usr/bin/python

from PyQt5 import QtGui, QtCore, QtWidgets
import sys

import IHM


class IHMViewer(QtWidgets.QMainWindow, IHM.Ui_IHM):
    def __init__(self, parent=None):
        super(IHMViewer, self).__init__(parent)
        self.setupUi(self)

    def main(self):
        self.show()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    IHM = IHMViewer()
    IHM.main()
    app.exec_()