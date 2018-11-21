# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IHM.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from message_builder import message_builder

class Ui_IHM(object):

    def on_button_pressed(self, button):
        if button == "automatic":
            self.commands['mode'] = 1
        elif button == "manual":
            self.commands['mode'] = 0
        else:
            self.commands[button] = 1
        self.bluetooth_thread.message = message_builder(self.commands)

    def on_button_released(self, button):
        self.commands[button] = 0
        self.bluetooth_thread.message = message_builder(self.commands)


    def onChange(self, i):  # changed!
        if (i == 1):
            self.commands['mode'] = 0
            self.bluetooth_thread.message = message_builder(self.commands)
            self.manual.setChecked(True)
    def setupUi(self, IHM, bluetooth_thread, commands):
        self.bluetooth_thread = bluetooth_thread
        self.commands = commands
        IHM.setObjectName("IHM")
        IHM.resize(970, 623)
        IHM.setMinimumSize(QtCore.QSize(779, 363))
        self.centralwidget = QtWidgets.QWidget(IHM)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 5, 960, 613))
        self.tabWidget.setObjectName("tabWidget")
        self.pilot_tab = QtWidgets.QWidget()
        self.pilot_tab.setObjectName("pilot_tab")

        self.logo = QtWidgets.QLabel(self.pilot_tab)
        self.logo.setGeometry(QtCore.QRect(640, -50, 300, 300))
        self.logo.setObjectName("logo")

        self.progressBar = QtWidgets.QProgressBar(self.pilot_tab)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(110, 90, 201, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 119, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 119, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.progressBar.setPalette(palette)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setFormat("%p mm/s")

        self.manual = QtWidgets.QRadioButton(self.pilot_tab)
        self.manual.setGeometry(QtCore.QRect(460, 120, 115, 22))
        self.manual.setMinimumSize(QtCore.QSize(115, 22))
        self.manual.setChecked(True)
        self.manual.setObjectName("manual")

        self.speed = QtWidgets.QLabel(self.pilot_tab)
        self.speed.setGeometry(QtCore.QRect(110, 60, 66, 17))
        self.speed.setMinimumSize(QtCore.QSize(66, 17))

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.speed.setFont(font)
        self.speed.setObjectName("speed")

        self.right = QtWidgets.QPushButton(self.pilot_tab)
        self.right.setGeometry(QtCore.QRect(300, 320, 97, 71))
        self.right.setMinimumSize(QtCore.QSize(97, 71))
        self.right.setObjectName("right")

        self.left = QtWidgets.QPushButton(self.pilot_tab)
        self.left.setGeometry(QtCore.QRect(100, 320, 97, 71))
        self.left.setMinimumSize(QtCore.QSize(97, 71))
        self.left.setObjectName("left")

        self.backward = QtWidgets.QPushButton(self.pilot_tab)
        self.backward.setGeometry(QtCore.QRect(200, 360, 97, 71))
        self.backward.setMinimumSize(QtCore.QSize(97, 71))
        self.backward.setObjectName("backward")

        self.mode = QtWidgets.QLabel(self.pilot_tab)
        self.mode.setGeometry(QtCore.QRect(460, 60, 66, 17))
        self.mode.setMinimumSize(QtCore.QSize(66, 17))

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.mode.setFont(font)
        self.mode.setObjectName("mode")

        self.forward = QtWidgets.QPushButton(self.pilot_tab)
        self.forward.setGeometry(QtCore.QRect(200, 280, 97, 71))
        self.forward.setMinimumSize(QtCore.QSize(97, 71))
        self.forward.setObjectName("forward")

        self.automatic = QtWidgets.QRadioButton(self.pilot_tab)
        self.automatic.setGeometry(QtCore.QRect(460, 90, 115, 22))
        self.automatic.setMinimumSize(QtCore.QSize(115, 22))
        self.automatic.setObjectName("automatic")

        self.indicator = QtWidgets.QLabel(self.pilot_tab)
        self.indicator.setGeometry(QtCore.QRect(110, 160, 111, 17))
        self.indicator.setMinimumSize(QtCore.QSize(66, 17))

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.indicator.setFont(font)
        self.indicator.setObjectName("indicator")

        self.tabWidget.addTab(self.pilot_tab, "")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.down = QtWidgets.QPushButton(self.tab)
        self.down.setGeometry(QtCore.QRect(690, 360, 97, 71))
        self.down.setMinimumSize(QtCore.QSize(97, 71))
        self.down.setObjectName("down")

        self.logo_2 = QtWidgets.QLabel(self.tab)
        self.logo_2.setGeometry(QtCore.QRect(640, -50, 300, 300))
        self.logo_2.setObjectName("logo_2")

        self.progressBar_2 = QtWidgets.QProgressBar(self.tab)
        self.progressBar_2.setEnabled(True)
        self.progressBar_2.setGeometry(QtCore.QRect(110, 90, 201, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 119, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 119, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.progressBar_2.setPalette(palette)
        self.progressBar_2.setMaximum(100)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_2.setFormat("%p mm/s")
        self.manual_2 = QtWidgets.QRadioButton(self.tab)
        self.manual_2.setGeometry(QtCore.QRect(460, 90, 115, 22))
        self.manual_2.setMinimumSize(QtCore.QSize(115, 22))
        self.manual_2.setChecked(True)
        self.manual_2.setObjectName("manual_2")
        self.speed_2 = QtWidgets.QLabel(self.tab)
        self.speed_2.setGeometry(QtCore.QRect(110, 60, 66, 17))
        self.speed_2.setMinimumSize(QtCore.QSize(66, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.speed_2.setFont(font)
        self.speed_2.setObjectName("speed_2")
        self.right_2 = QtWidgets.QPushButton(self.tab)
        self.right_2.setGeometry(QtCore.QRect(300, 320, 97, 71))
        self.right_2.setMinimumSize(QtCore.QSize(97, 71))
        self.right_2.setObjectName("right_2")
        self.left_2 = QtWidgets.QPushButton(self.tab)
        self.left_2.setGeometry(QtCore.QRect(100, 320, 97, 71))
        self.left_2.setMinimumSize(QtCore.QSize(97, 71))
        self.left_2.setObjectName("left_2")
        self.backward_2 = QtWidgets.QPushButton(self.tab)
        self.backward_2.setGeometry(QtCore.QRect(200, 360, 97, 71))
        self.backward_2.setMinimumSize(QtCore.QSize(97, 71))
        self.backward_2.setObjectName("backward_2")
        self.mode_2 = QtWidgets.QLabel(self.tab)
        self.mode_2.setGeometry(QtCore.QRect(460, 60, 66, 17))
        self.mode_2.setMinimumSize(QtCore.QSize(66, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.mode_2.setFont(font)
        self.mode_2.setObjectName("mode_2")
        self.forward_2 = QtWidgets.QPushButton(self.tab)
        self.forward_2.setGeometry(QtCore.QRect(200, 280, 97, 71))
        self.forward_2.setMinimumSize(QtCore.QSize(97, 71))
        self.forward_2.setObjectName("forward_2")
        self.up = QtWidgets.QPushButton(self.tab)
        self.up.setGeometry(QtCore.QRect(690, 280, 97, 71))
        self.up.setMinimumSize(QtCore.QSize(97, 71))
        self.up.setObjectName("up")
        self.indicator_2 = QtWidgets.QLabel(self.tab)
        self.indicator_2.setGeometry(QtCore.QRect(110, 160, 111, 17))
        self.indicator_2.setMinimumSize(QtCore.QSize(66, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.indicator_2.setFont(font)
        self.indicator_2.setObjectName("indicator_2")
        self.mode_2.raise_()
        self.down.raise_()
        self.logo_2.raise_()
        self.progressBar_2.raise_()
        self.manual_2.raise_()
        self.speed_2.raise_()
        self.right_2.raise_()
        self.left_2.raise_()
        self.backward_2.raise_()
        self.forward_2.raise_()
        self.up.raise_()
        self.down.raise_()
        self.logo_2.raise_()
        self.progressBar_2.raise_()
        self.manual_2.raise_()
        self.speed_2.raise_()
        self.right_2.raise_()
        self.left_2.raise_()
        self.backward_2.raise_()
        self.mode_2.raise_()
        self.forward_2.raise_()
        self.up.raise_()
        self.indicator_2.raise_()
        self.tabWidget.addTab(self.tab, "")
        IHM.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(IHM)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1010, 25))
        self.menubar.setObjectName("menubar")
        IHM.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(IHM)
        self.statusbar.setObjectName("statusbar")
        IHM.setStatusBar(self.statusbar)

        self.tabWidget.currentChanged.connect(self.onChange)

        self.forward.pressed.connect(lambda: self.on_button_pressed('forward'))
        self.forward_2.pressed.connect(lambda: self.on_button_pressed('forward'))

        self.forward.released.connect(lambda: self.on_button_released('forward'))
        self.forward_2.released.connect(lambda: self.on_button_released('forward'))

        self.left.pressed.connect(lambda: self.on_button_pressed('left'))
        self.left_2.pressed.connect(lambda: self.on_button_pressed('left'))

        self.left.released.connect(lambda: self.on_button_released('left'))
        self.left_2.released.connect(lambda: self.on_button_released('left'))

        self.right.pressed.connect(lambda: self.on_button_pressed('right'))
        self.right_2.pressed.connect(lambda: self.on_button_pressed('right'))

        self.right.released.connect(lambda: self.on_button_released('right'))
        self.right_2.released.connect(lambda: self.on_button_released('right'))

        self.backward.pressed.connect(lambda: self.on_button_pressed('backward'))
        self.backward_2.pressed.connect(lambda: self.on_button_pressed('backward'))

        self.backward.released.connect(lambda: self.on_button_released('backward'))
        self.backward_2.released.connect(lambda: self.on_button_released('backward'))

        self.up.pressed.connect(lambda: self.on_button_pressed('up'))

        self.up.released.connect(lambda: self.on_button_released('up'))

        self.down.pressed.connect(lambda: self.on_button_pressed('down'))

        self.down.released.connect(lambda: self.on_button_released('down'))

        self.automatic.pressed.connect(lambda: self.on_button_pressed("automatic"))
        self.manual.pressed.connect(lambda: self.on_button_pressed("manual"))

        self.retranslateUi(IHM)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(IHM)

    def retranslateUi(self, IHM):
        _translate = QtCore.QCoreApplication.translate
        IHM.setWindowTitle(_translate("IHM", "MainWindow"))
        self.logo.setText(_translate("IHM", "TextLabel"))
        self.progressBar.setFormat(_translate("IHM", "%p"))
        self.manual.setText(_translate("IHM", "Manual"))
        self.speed.setText(_translate("IHM", "Speed"))
        self.right.setText(_translate("IHM", "Right"))
        self.left.setText(_translate("IHM", "Left"))
        self.backward.setText(_translate("IHM", "Backward"))
        self.mode.setText(_translate("IHM", "Mode"))
        self.forward.setText(_translate("IHM", "Forward"))
        self.automatic.setText(_translate("IHM", "Automatic"))
        self.indicator.setText(_translate("IHM", "Light Indicator"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pilot_tab), _translate("IHM", "IHM Pilot"))
        self.down.setText(_translate("IHM", "Down"))
        self.logo_2.setText(_translate("IHM", "TextLabel"))
        self.progressBar_2.setFormat(_translate("IHM", "%p"))
        self.manual_2.setText(_translate("IHM", "Manual"))
        self.speed_2.setText(_translate("IHM", "Speed"))
        self.right_2.setText(_translate("IHM", "Right"))
        self.left_2.setText(_translate("IHM", "Left"))
        self.backward_2.setText(_translate("IHM", "Backward"))
        self.mode_2.setText(_translate("IHM", "Mode"))
        self.forward_2.setText(_translate("IHM", "Forward"))
        self.up.setText(_translate("IHM", "Up"))
        self.indicator_2.setText(_translate("IHM", "Light Indicator"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("IHM", "IHM Manu"))
        self.logo.setPixmap(QtGui.QPixmap("./logo200.png"))
        self.logo_2.setPixmap(QtGui.QPixmap("./logo200.png"))


# Form implementation generated from reading ui file 'IHM.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# class Ui_IHM(object):
#
#
#     def on_button_pressed(self, button):
#         if button == "automatic":
#             self.commands['mode'] = 1
#         elif button == "manual":
#             self.commands['mode'] = 0
#         else:
#             self.commands[button] = 1
#         self.bluetooth_thread.message = message_builder(self.commands)
#
#     def on_button_released(self, button):
#         self.commands[button] = 0
#         self.bluetooth_thread.message = message_builder(self.commands)
#
#
#
#     def setupUi(self, IHM, bluetooth_thread, commands):
#         self.bluetooth_thread = bluetooth_thread
#         self.commands = commands
#
#         IHM.setObjectName("IHM")
#         IHM.resize(1010, 683)
#         IHM.setMinimumSize(QSize(779, 363))
#         font = QFont()
#         font.setBold(True)
#         font.setWeight(75)
#
#         self.setAutoFillBackground(True)
#         p = self.palette()
#         p.setColor(self.backgroundRole(), Qt.white)
#         self.setPalette(p)
#
#         self.centralwidget = QWidget(IHM)
#         self.centralwidget.setObjectName("centralwidget")
#
#         self.label = QLabel(self.centralwidget)
#         self.label.setGeometry(QRect(410, 30, 66, 17))
#         self.label.setMinimumSize(QSize(66, 17))
#         self.label.setObjectName("label")
#         self.label.setFont(font)
#
#
#         self.label_2 = QLabel(self.centralwidget)
#         self.label_2.setGeometry(QRect(60, 30, 66, 17))
#         self.label_2.setMinimumSize(QSize(66, 17))
#         self.label_2.setObjectName("label_2")
#         self.label_2.setFont(font)
#
#
#         self.label_4 = QLabel(self.centralwidget)
#         self.label_4.setGeometry(QRect(550, -60, 300, 300))
#         self.label_4.setObjectName("label_4")
#
#         self.pushButton = QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QRect(460, 150, 97, 71))
#         self.pushButton.setMinimumSize(QSize(97, 71))
#         self.pushButton.setObjectName("pushButton")
#
#         self.pushButton_2 = QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QRect(360, 190, 97, 71))
#         self.pushButton_2.setMinimumSize(QSize(97, 71))
#         self.pushButton_2.setObjectName("pushButton_2")
#
#         self.pushButton_3 = QPushButton(self.centralwidget)
#         self.pushButton_3.setGeometry(QRect(560, 190, 97, 71))
#         self.pushButton_3.setMinimumSize(QSize(97, 71))
#         self.pushButton_3.setObjectName("pushButton_3")
#
#         self.pushButton_4 = QPushButton(self.centralwidget)
#         self.pushButton_4.setGeometry(QRect(460, 230, 97, 71))
#         self.pushButton_4.setMinimumSize(QSize(97, 71))
#         self.pushButton_4.setObjectName("pushButton_4")
#
#         self.radioButton = QRadioButton(self.centralwidget)
#         self.radioButton.setGeometry(QRect(410, 60, 115, 22))
#         self.radioButton.setMinimumSize(QSize(115, 22))
#         self.radioButton.setObjectName("radioButton")
#
#         self.radioButton_2 = QRadioButton(self.centralwidget)
#         self.radioButton_2.setGeometry(QRect(410, 90, 115, 22))
#         self.radioButton_2.setMinimumSize(QSize(115, 22))
#         self.radioButton_2.setChecked(True)
#         self.radioButton_2.setObjectName("radioButton_2")
#
#         self.pushButton_5 = QPushButton(self.centralwidget)
#         self.pushButton_5.setGeometry(QRect(70, 240, 97, 71))
#         self.pushButton_5.setMinimumSize(QSize(97, 71))
#         self.pushButton_5.setObjectName("pushButton_5")
#
#         self.pushButton_6 = QPushButton(self.centralwidget)
#         self.pushButton_6.setGeometry(QRect(70, 160, 97, 71))
#         self.pushButton_6.setMinimumSize(QSize(97, 71))
#         self.pushButton_6.setObjectName("pushButton_6")
#
#         self.progressBar = QProgressBar(self.centralwidget)
#         self.progressBar.setEnabled(True)
#         self.progressBar.setGeometry(QRect(60, 60, 201, 23))
#
#         palette = QPalette()
#         brush = QBrush(QColor(240, 119, 70))
#         brush.setStyle(Qt.SolidPattern)
#         palette.setBrush(QPalette.Active, QPalette.Highlight, brush)
#         brush = QBrush(QColor(240, 119, 70))
#         brush.setStyle(Qt.SolidPattern)
#         palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
#         brush = QBrush(QColor(240, 240, 240))
#         brush.setStyle(Qt.SolidPattern)
#         palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush)
#
#         self.progressBar.setFormat("%p mm/s")
#         self.progressBar.setPalette(palette)
#         self.progressBar.setMaximum(100)
#         self.progressBar.setProperty("value", 1)
#         self.progressBar.setObjectName("progressBar")
#
#         IHM.setCentralWidget(self.centralwidget)
#
#         self.menubar = QMenuBar(IHM)
#         self.menubar.setGeometry(QRect(0, 0, 779, 25))
#         self.menubar.setObjectName("menubar")
#         IHM.setMenuBar(self.menubar)
#
#         self.statusbar = QStatusBar(IHM)
#         self.statusbar.setObjectName("statusbar")
#         IHM.setStatusBar(self.statusbar)
#
#
        # self.pushButton.pressed.connect(lambda: self.on_button_pressed('up'))
        # self.pushButton.released.connect(lambda: self.on_button_released('up'))
        #
        # self.pushButton_2.pressed.connect(lambda: self.on_button_pressed('left'))
        # self.pushButton_2.released.connect(lambda: self.on_button_released('left'))
        #
        # self.pushButton_3.pressed.connect(lambda: self.on_button_pressed('right'))
        # self.pushButton_3.released.connect(lambda: self.on_button_released('right'))
        #
        # self.pushButton_4.pressed.connect(lambda: self.on_button_pressed('down'))
        # self.pushButton_4.released.connect(lambda: self.on_button_released('down'))
        #
        # self.pushButton_5.pressed.connect(lambda: self.on_button_pressed('arm_up'))
        # self.pushButton_5.released.connect(lambda: self.on_button_released('arm_up'))
        #
        # self.pushButton_6.pressed.connect(lambda: self.on_button_pressed('arm_down'))
        # self.pushButton_6.released.connect(lambda: self.on_button_released('arm_down'))
        #
        # self.radioButton.pressed.connect(lambda: self.on_button_pressed("automatic"))
        # self.radioButton_2.pressed.connect(lambda: self.on_button_pressed("manual"))
#
#
#         self.retranslateUi(IHM)
#         QMetaObject.connectSlotsByName(IHM)
#
#
#     def retranslateUi(self, IHM):
#         _translate = QCoreApplication.translate
#         IHM.setWindowTitle(_translate("IHM", "IHM - ROBAFIS - INSATOMIQUE"))
#         self.label.setText(_translate("IHM", "Mode"))
#         self.label_2.setText(_translate("IHM", "Speed"))
#         self.label_4.setPixmap(QPixmap("./logo200.png"))
#         self.pushButton.setText(_translate("IHM", "Forward"))
#         self.pushButton_2.setText(_translate("IHM", "Left"))
#         self.pushButton_3.setText(_translate("IHM", "Right"))
#         self.pushButton_4.setText(_translate("IHM", "Backward"))
#         self.radioButton.setText(_translate("IHM", "Automatic"))
#         self.radioButton_2.setText(_translate("IHM", "Manual"))
#         self.pushButton_5.setText(_translate("IHM", "Down"))
#         self.pushButton_6.setText(_translate("IHM", "Up"))
