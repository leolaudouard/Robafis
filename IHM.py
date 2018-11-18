# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IHM.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from message_builder import message_builder

class Ui_IHM(object):


    def on_button_pressed(self, button):
        if button == "automatic":
            self.commands['mode'] = 1
            print(self.speed)
        elif button == "manual":
            self.commands['mode'] = 0
        else:
            self.commands[button] = 1
        self.bluetooth_thread.message = message_builder(self.commands)

    def on_button_released(self, button):
        self.commands[button] = 0
        self.bluetooth_thread.message = message_builder(self.commands)



    def setupUi(self, IHM, bluetooth_thread, commands):
        self.bluetooth_thread = bluetooth_thread
        self.commands = commands

        IHM.setObjectName("IHM")
        IHM.resize(779, 379)
        IHM.setMinimumSize(QSize(779, 363))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        self.centralwidget = QWidget(IHM)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(410, 30, 66, 17))
        self.label.setMinimumSize(QSize(66, 17))
        self.label.setObjectName("label")
        self.label.setFont(font)


        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QRect(60, 30, 66, 17))
        self.label_2.setMinimumSize(QSize(66, 17))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)


        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setGeometry(QRect(550, -60, 300, 300))
        self.label_4.setObjectName("label_4")

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(460, 150, 97, 71))
        self.pushButton.setMinimumSize(QSize(97, 71))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QRect(360, 190, 97, 71))
        self.pushButton_2.setMinimumSize(QSize(97, 71))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QRect(560, 190, 97, 71))
        self.pushButton_3.setMinimumSize(QSize(97, 71))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QRect(460, 230, 97, 71))
        self.pushButton_4.setMinimumSize(QSize(97, 71))
        self.pushButton_4.setObjectName("pushButton_4")

        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QRect(410, 60, 115, 22))
        self.radioButton.setMinimumSize(QSize(115, 22))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QRect(410, 90, 115, 22))
        self.radioButton_2.setMinimumSize(QSize(115, 22))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QRect(70, 240, 97, 71))
        self.pushButton_5.setMinimumSize(QSize(97, 71))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QRect(70, 160, 97, 71))
        self.pushButton_6.setMinimumSize(QSize(97, 71))
        self.pushButton_6.setObjectName("pushButton_6")

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QRect(60, 60, 201, 23))

        palette = QPalette()
        brush = QBrush(QColor(240, 119, 70))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush)
        brush = QBrush(QColor(240, 119, 70))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        brush = QBrush(QColor(240, 240, 240))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush)

        self.progressBar.setFormat("%p mm/s")
        self.progressBar.setPalette(palette)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

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

        self.radioButton.pressed.connect(lambda: self.on_button_pressed("automatic"))
        self.radioButton_2.pressed.connect(lambda: self.on_button_pressed("manual"))


        self.retranslateUi(IHM)
        QMetaObject.connectSlotsByName(IHM)


    def retranslateUi(self, IHM):
        _translate = QCoreApplication.translate
        IHM.setWindowTitle(_translate("IHM", "IHM - ROBAFIS - INSATOMIQUE"))
        self.label.setText(_translate("IHM", "Mode"))
        self.label_2.setText(_translate("IHM", "Speed"))
        self.label_4.setPixmap(QPixmap("logo200.png"))
        self.pushButton.setText(_translate("IHM", "Forward"))
        self.pushButton_2.setText(_translate("IHM", "Left"))
        self.pushButton_3.setText(_translate("IHM", "Right"))
        self.pushButton_4.setText(_translate("IHM", "Backward"))
        self.radioButton.setText(_translate("IHM", "Automatic"))
        self.radioButton_2.setText(_translate("IHM", "Manual"))
        self.pushButton_5.setText(_translate("IHM", "Down"))
        self.pushButton_6.setText(_translate("IHM", "Up"))
