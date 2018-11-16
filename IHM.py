# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IHM.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_IHM(object):

    def on_button_pressed(self, button):
        #TODO: Update Bluetooth thread message
        if button == 'up':
            print('pressed')
        elif button == 'down':
            print('pressed')
        elif button == 'right':
            print('pressed')
        elif button == 'left':
            print('pressed')
        elif button == 'arm_up':
            print('pressed')
        elif button == 'arm_down':
            print('pressed')


    def on_button_released(self, button):
        # TODO: Update Bluetooth thread message
        if button == 'up':
            print ('release')
        elif button == 'down':
            print('release')
        elif button == 'right':
            print('release')
        elif button == 'left':
            print('release')
        elif button == 'arm_up':
            print('release')
        elif button == 'arm_down':
            print('release')


    def setupUi(self, IHM):
        IHM.setObjectName("IHM")
        IHM.resize(779, 363)
        IHM.setMinimumSize(QSize(500, 200))

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        self.centralwidget = QWidget(IHM)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(360, 50, 66, 17))
        self.label.setMinimumSize(QSize(66, 17))
        self.label.setObjectName("label")

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QRect(280, 50, 66, 17))
        self.label_2.setMinimumSize(QSize(66, 17))
        self.label_2.setObjectName("label_2")

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(QRect(420, 50, 66, 17))
        self.label_3.setMinimumSize(QSize(66, 17))
        self.label_3.setObjectName("label_3")

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setGeometry(QRect(20, -60, 300, 300))
        self.label_4.setObjectName("label_4")

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(560, 140, 97, 71))
        self.pushButton.setMinimumSize(QSize(97, 71))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QRect(460, 180, 97, 71))
        self.pushButton_2.setMinimumSize(QSize(97, 71))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QRect(660, 180, 97, 71))
        self.pushButton_3.setMinimumSize(QSize(97, 71))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QRect(560, 220, 97, 71))
        self.pushButton_4.setMinimumSize(QSize(97, 71))
        self.pushButton_4.setObjectName("pushButton_4")

        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QRect(550, 30, 115, 22))
        self.radioButton.setMinimumSize(QSize(115, 22))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QRect(550, 60, 115, 22))
        self.radioButton_2.setMinimumSize(QSize(115, 22))
        self.radioButton_2.setObjectName("radioButton_2")

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QRect(110, 220, 97, 71))
        self.pushButton_5.setMinimumSize(QSize(97, 71))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QRect(110, 140, 97, 71))
        self.pushButton_6.setMinimumSize(QSize(97, 71))
        self.pushButton_6.setObjectName("pushButton_6")

        IHM.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(IHM)
        self.menubar.setGeometry(QRect(0, 0, 779, 25))
        self.menubar.setObjectName("menubar")
        IHM.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(IHM)
        self.statusbar.setObjectName("statusbar")
        IHM.setStatusBar(self.statusbar)


        self.pushButton.pressed.connect(lambda: self.on_button_pressed('up'))
        self.pushButton.released.connect(lambda: self.on_button_released('up'))

        self.pushButton_2.pressed.connect(lambda: self.on_button_pressed('left'))
        self.pushButton_2.released.connect(lambda: self.on_button_released('left'))

        self.pushButton_3.pressed.connect(lambda: self.on_button_pressed('right'))
        self.pushButton_3.released.connect(lambda: self.on_button_released('right'))

        self.pushButton_4.pressed.connect(lambda: self.on_button_pressed('down'))
        self.pushButton_4.released.connect(lambda: self.on_button_released('down'))

        self.pushButton_5.pressed.connect(lambda: self.on_button_pressed('arm_up'))
        self.pushButton_5.released.connect(lambda: self.on_button_released('arm_up'))

        self.pushButton_6.pressed.connect(lambda: self.on_button_pressed('arm_down'))
        self.pushButton_6.released.connect(lambda: self.on_button_released('arm_down'))

        self.retranslateUi(IHM)
        QMetaObject.connectSlotsByName(IHM)


    def retranslateUi(self, IHM):
        _translate = QCoreApplication.translate
        IHM.setWindowTitle(_translate("IHM", "IHM - ROBAFIS - INSATOMIQUE"))
        self.label.setText(_translate("IHM", "0"))
        self.label_2.setText(_translate("IHM", "Speed"))
        self.label_3.setText(_translate("IHM", "mm/s"))
        self.label_4.setPixmap(QPixmap("logo200.png"))
        self.pushButton.setText(_translate("IHM", "Forward"))
        self.pushButton_2.setText(_translate("IHM", "Left"))
        self.pushButton_3.setText(_translate("IHM", "Right"))
        self.pushButton_4.setText(_translate("IHM", "Backward"))
        self.radioButton.setText(_translate("IHM", "Automatic"))
        self.radioButton_2.setText(_translate("IHM", "Manual"))
        self.pushButton_5.setText(_translate("IHM", "Down"))
        self.pushButton_6.setText(_translate("IHM", "Up"))
