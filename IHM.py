# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IHM.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from message_builder import message_builder

class Ui_IHM(object):

    def updateValue(self, value, commands, speed_limit, connection, lineFollower):
        self.progressBar.setValue(value)
        self.progressBar_2.setValue(value)
        if lineFollower == '3':
            if self.led_line_state != 'white':
                self.led_line_state = 'white'
                self.led_line.setPixmap(QtGui.QPixmap("./images/leds/white_led.png"))
        else:
            if self.led_line_state != 'black':
                self.led_line_state = 'black'
                self.led_line.setPixmap(QtGui.QPixmap("./images/leds/black_led.png"))

        if connection:
            if self.led_bluetooth_state != 'blue':
                self.led_bluetooth_state = 'blue'
                self.led_bluetooth.setPixmap(QtGui.QPixmap("./images/leds/blue_led.png"))

        else:
            if (self.led_bluetooth_state != 'red'):
                self.led_bluetooth_state = 'red'
                self.led_bluetooth.setPixmap(QtGui.QPixmap("./images/leds/red_led.png"))

        if speed_limit:
            if self.led_speed_state != 'red':
                self.led_speed_state = 'red'
                self.led_speed.setPixmap(QtGui.QPixmap("./images/leds/red_led.png"))

        else:
            if (self.led_speed_state != 'green'):
                self.led_speed_state = 'green'
                self.led_speed.setPixmap(QtGui.QPixmap("./images/leds/green_led.png"))


        if commands['forward']:
            self.forward.setDown(True)
            self.forward_2.setDown(True)
        else:
            self.forward.setDown(False)
            self.forward_2.setDown(False)

        if commands['backward']:
            self.backward.setDown(True)
            self.backward_2.setDown(True)
        else:
            self.backward.setDown(False)
            self.backward_2.setDown(False)

        if commands['left']:
            self.left.setDown(True)
            self.left_2.setDown(True)
        else:
            self.left.setDown(False)
            self.left_2.setDown(False)

        if commands['right']:
            self.right.setDown(True)
            self.right_2.setDown(True)
        else:
            self.right.setDown(False)
            self.right_2.setDown(False)

        if self.tabWidget.currentIndex() == 1:
            if commands['up']:
                self.up.setDown(True)
            else:
                self.up.setDown(False)

            if commands['down']:
                self.down.setDown(True)
            else:
                self.down.setDown(False)

    def updateButton(self, button, Bool):
        if button == 'forward':
            self.forward.setDown(Bool)
            self.forward_2.setDown(Bool)


    def on_button_pressed(self, button):
        if button == "automatic":
            self.commands['mode'] = 1
        elif button == "manual":
            self.commands['mode'] = 0
        elif button == "low_speed":
            self.commands['speedmode'] = 1
            self.high_speed.setChecked(False)
            self.speed_limit_img.setPixmap(QtGui.QPixmap("./images/zone15.png"))
        elif button == "high_speed":
            self.commands['speedmode'] = 0
            self.low_speed.setChecked(False)
            self.speed_limit_img.setPixmap(QtGui.QPixmap("./images/zone80.png"))
        elif button == "stop":
            if self.commands['mode'] == 1:
                self.automatic.setChecked(False)
                self.manual.setChecked(True)
            for key in self.commands:
                if key != "speedmode":
                    self.commands[key] = 0


        else:
            self.commands[button] = 1

    def on_combobox_changed(self, value):
        if value == 'Timer':
            self.commands['stopMode'] = 1
        else:
            self.commands['stopMode'] = 0


    def on_button_released(self, button):
        self.commands[button] = 0


    def onChange(self, i):  # changed!
        if (i == 1):
            self.commands['mode'] = 0
            self.manual.setChecked(True)

    def setupUi(self, IHM, commands):
        self.commands = commands

        screen_height = 1080
        screen_width = 1920

        buttons_center = [screen_width/4, 600]
        buttons_size = [180, 120]

        font = QtGui.QFont('SansSerif', 20)
        font.setBold(True)
        font.setWeight(75)

        IHM.setObjectName("IHM")
        IHM.resize(screen_width, screen_height)
        IHM.setMinimumSize(QtCore.QSize(screen_width*0.5, screen_height*0.5))

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.white)
        self.setPalette(p)

        self.centralwidget = QtWidgets.QWidget(IHM)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 5, screen_width*0.95 , screen_height*0.92))
        self.tabWidget.setObjectName("tabWidget")



        self.pilot_tab = QtWidgets.QWidget()
        self.pilot_tab.setObjectName("pilot_tab")

        self.comboBox = QtWidgets.QComboBox(self.pilot_tab)
        self.comboBox.setGeometry(QtCore.QRect(460, 190, 115, 22))
        self.comboBox.setObjectName("comboBox_2")
        self.comboBox.addItem("")
        self.comboBox.addItem("")


        p.setColor(self.pilot_tab.backgroundRole(), QtCore.Qt.white)
        self.setPalette(p)

        self.logo = QtWidgets.QLabel(self.pilot_tab)
        self.logo.setGeometry(QtCore.QRect(1170, -50, 500, 500))
        self.logo.setObjectName("logo")

        self.speed_limit_img = QtWidgets.QLabel(self.centralwidget)
        self.speed_limit_img.setGeometry(QtCore.QRect(100, 300, 300, 300))
        self.speed_limit_img.setObjectName("speed_limit_img")

        self.progressBar = QtWidgets.QProgressBar(self.pilot_tab)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(110, 110, 201, 23))

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

        self.led_bluetooth = QtWidgets.QLabel(self.centralwidget)
        self.led_bluetooth.setGeometry(QtCore.QRect(810, 150, 40, 40))
        self.led_bluetooth.setObjectName("led_bluetooth")
        self.led_bluetooth_state = 'red'

        self.led_speed = QtWidgets.QLabel(self.centralwidget)
        self.led_speed.setGeometry(QtCore.QRect(810, 200, 40, 40))
        self.led_speed.setObjectName("led_bluetooth")
        self.led_speed_state = 'green'

        self.led_line = QtWidgets.QLabel(self.centralwidget)
        self.led_line.setGeometry(QtCore.QRect(810, 250, 40, 40))
        self.led_line.setObjectName("led_line")
        self.led_line_state = 'white'

        self.bluetooth = QtWidgets.QLabel(self.centralwidget)
        self.bluetooth.setGeometry(QtCore.QRect(860, 103, 160, 130))
        self.bluetooth.setMinimumSize(QtCore.QSize(66, 17))
        self.bluetooth.setObjectName("bluetooth")

        self.line = QtWidgets.QLabel(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(860, 205, 160, 130))
        self.line.setMinimumSize(QtCore.QSize(66, 17))
        self.line.setObjectName("line")

        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(1235, 400, buttons_size[0], buttons_size[1]))
        self.stop.setMinimumSize(QtCore.QSize(97, 71))
        self.stop.setObjectName("stop")


        p = self.stop.palette()
        p.setColor(self.stop.backgroundRole(), QtCore.Qt.red)
        self.stop.setPalette(p)

        self.speed_limit = QtWidgets.QLabel(self.centralwidget)
        self.speed_limit.setGeometry(QtCore.QRect(860, 155, 130, 130))
        self.speed_limit.setMinimumSize(QtCore.QSize(66, 17))
        self.speed_limit.setObjectName("speed_limit")

        self.speed = QtWidgets.QLabel(self.pilot_tab)
        self.speed.setGeometry(QtCore.QRect(110, 60, 100, 40))
        self.speed.setMinimumSize(QtCore.QSize(66, 17))
        self.speed.setFont(font)
        self.speed.setObjectName("speed")

        self.right = QtWidgets.QPushButton(self.pilot_tab)
        self.right.setGeometry(QtCore.QRect(buttons_center[0] + buttons_size[0], buttons_center[1], buttons_size[0], buttons_size[1]))
        self.right.setMinimumSize(QtCore.QSize(97, 71))
        self.right.setObjectName("right")

        self.left = QtWidgets.QPushButton(self.pilot_tab)
        self.left.setGeometry(QtCore.QRect(buttons_center[0] - buttons_size[0], buttons_center[1], buttons_size[0], buttons_size[1]))
        self.left.setMinimumSize(QtCore.QSize(97, 71))
        self.left.setObjectName("left")

        self.forward = QtWidgets.QPushButton(self.pilot_tab)
        self.forward.setGeometry(QtCore.QRect(buttons_center[0], buttons_center[1] - buttons_size[1]/2, buttons_size[0], buttons_size[1]))
        self.forward.setMinimumSize(QtCore.QSize(97, 71))
        self.forward.setObjectName("forward")

        self.backward = QtWidgets.QPushButton(self.pilot_tab)
        self.backward.setGeometry(QtCore.QRect(buttons_center[0], buttons_center[1] + buttons_size[1]/2, buttons_size[0], buttons_size[1]))
        self.backward.setMinimumSize(QtCore.QSize(97, 71))
        self.backward.setObjectName("backward")

        self.mode = QtWidgets.QLabel(self.pilot_tab)
        self.mode.setGeometry(QtCore.QRect(460, 60, 100, 40))
        self.mode.setMinimumSize(QtCore.QSize(66, 17))
        self.mode.setFont(font)
        self.mode.setObjectName("mode")

        self.automatic = QtWidgets.QRadioButton(self.pilot_tab)
        self.automatic.setGeometry(QtCore.QRect(460, 110, 115, 22))
        self.automatic.setMinimumSize(QtCore.QSize(115, 22))
        self.automatic.setObjectName("automatic")

        self.manual = QtWidgets.QRadioButton(self.pilot_tab)
        self.manual.setGeometry(QtCore.QRect(460, 140, 115, 22))
        self.manual.setMinimumSize(QtCore.QSize(115, 22))
        self.manual.setChecked(True)
        self.manual.setObjectName("manual")


        self.speed_mode = QtWidgets.QLabel(self.centralwidget)
        self.speed_mode.setGeometry(QtCore.QRect(115, 200, 200, 40))
        self.speed_mode.setMinimumSize(QtCore.QSize(66, 17))
        self.speed_mode.setFont(font)
        self.speed_mode.setObjectName("speed_mode")

        self.high_speed= QtWidgets.QRadioButton(self.centralwidget)
        self.high_speed.setGeometry(QtCore.QRect(120, 240, 100, 40))
        self.high_speed.setMinimumSize(QtCore.QSize(115, 22))
        self.high_speed.setObjectName("automatic")
        self.high_speed.setChecked(True)

        self.low_speed = QtWidgets.QRadioButton(self.centralwidget)
        self.low_speed .setGeometry(QtCore.QRect(120, 270, 100, 40))
        self.low_speed .setMinimumSize(QtCore.QSize(115, 22))
        self.low_speed .setObjectName("manual")

        self.indicator = QtWidgets.QLabel(self.centralwidget)
        self.indicator.setGeometry(QtCore.QRect(810, 90, 400, 40))
        self.indicator.setMinimumSize(QtCore.QSize(66, 17))
        self.indicator.setFont(font)
        self.indicator.setObjectName("indicator")

        self.tabWidget.addTab(self.pilot_tab, "")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")


        self.down = QtWidgets.QPushButton(self.tab)
        self.down.setGeometry(QtCore.QRect(buttons_center[0] + 750, buttons_center[1] + buttons_size[1]/2, buttons_size[0], buttons_size[1]))
        self.down.setMinimumSize(QtCore.QSize(97, 71))
        self.down.setObjectName("down")

        self.up = QtWidgets.QPushButton(self.tab)
        self.up.setGeometry(QtCore.QRect(buttons_center[0] + 750, buttons_center[1] - buttons_size[1]/2, buttons_size[0], buttons_size[1]))
        self.up.setMinimumSize(QtCore.QSize(97, 71))
        self.up.setObjectName("up")

        self.logo_2 = QtWidgets.QLabel(self.tab)
        self.logo_2.setGeometry(QtCore.QRect(1170, -50, 500, 500))
        self.logo_2.setObjectName("logo_2")

        self.progressBar_2 = QtWidgets.QProgressBar(self.tab)
        self.progressBar_2.setEnabled(True)
        self.progressBar_2.setGeometry(QtCore.QRect(110, 110, 201, 23))

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
        self.progressBar_2.setFormat("%p mm/s")
        self.progressBar_2.setMaximum(100)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")


        self.manual_2 = QtWidgets.QRadioButton(self.tab)
        self.manual_2.setGeometry(QtCore.QRect(460, 110, 115, 22))
        self.manual_2.setMinimumSize(QtCore.QSize(115, 22))
        self.manual_2.setChecked(True)
        self.manual_2.setObjectName("manual_2")
        self.manual_2.setEnabled(False)

        self.speed_2 = QtWidgets.QLabel(self.tab)
        self.speed_2.setGeometry(QtCore.QRect(110, 60, 100, 40))
        self.speed_2.setMinimumSize(QtCore.QSize(66, 17))
        self.speed_2.setFont(font)
        self.speed_2.setObjectName("speed_2")

        self.right_2 = QtWidgets.QPushButton(self.tab)
        self.right_2.setGeometry(QtCore.QRect(buttons_center[0] + buttons_size[0], buttons_center[1], buttons_size[0], buttons_size[1]))
        self.right_2.setMinimumSize(QtCore.QSize(97, 71))
        self.right_2.setObjectName("right_2")

        self.left_2 = QtWidgets.QPushButton(self.tab)
        self.left_2.setGeometry(QtCore.QRect(buttons_center[0] - buttons_size[0], buttons_center[1], buttons_size[0], buttons_size[1]))
        self.left_2.setMinimumSize(QtCore.QSize(97, 71))
        self.left_2.setObjectName("left_2")

        self.forward_2 = QtWidgets.QPushButton(self.tab)
        self.forward_2.setGeometry(QtCore.QRect(buttons_center[0], buttons_center[1] - buttons_size[1] / 2, buttons_size[0], buttons_size[1]))
        self.forward_2.setMinimumSize(QtCore.QSize(97, 71))
        self.forward_2.setObjectName("forward_2")

        self.backward_2 = QtWidgets.QPushButton(self.tab)
        self.backward_2.setGeometry(QtCore.QRect(buttons_center[0], buttons_center[1] + buttons_size[1] / 2, buttons_size[0], buttons_size[1]))
        self.backward_2.setMinimumSize(QtCore.QSize(97, 71))
        self.backward_2.setObjectName("backward_2")

        self.mode_2 = QtWidgets.QLabel(self.tab)
        self.mode_2.setGeometry(QtCore.QRect(460, 60, 100, 40))
        self.mode_2.setMinimumSize(QtCore.QSize(66, 17))
        self.mode_2.setFont(font)
        self.mode_2.setObjectName("mode_2")


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
        self.speed_limit_img.raise_()
        self.manual_2.raise_()
        self.speed_2.raise_()
        self.right_2.raise_()
        self.left_2.raise_()
        self.backward_2.raise_()
        self.mode_2.raise_()
        self.forward_2.raise_()
        self.up.raise_()
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
        self.stop.pressed.connect(lambda: self.on_button_pressed('stop'))

        self.up.released.connect(lambda: self.on_button_released('up'))

        self.down.pressed.connect(lambda: self.on_button_pressed('down'))

        self.down.released.connect(lambda: self.on_button_released('down'))

        self.automatic.pressed.connect(lambda: self.on_button_pressed("automatic"))
        self.manual.pressed.connect(lambda: self.on_button_pressed("manual"))

        self.low_speed.pressed.connect(lambda : self.on_button_pressed("low_speed"))
        self.high_speed.pressed.connect(lambda : self.on_button_pressed("high_speed"))

        self.comboBox.currentTextChanged.connect(self.on_combobox_changed)

        self.retranslateUi(IHM)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(IHM)

    def retranslateUi(self, IHM):
        _translate = QtCore.QCoreApplication.translate
        IHM.setWindowTitle(_translate("IHM", "MainWindow"))
        self.progressBar.setFormat(_translate("IHM", "%p"))
        self.manual.setText(_translate("IHM", "Manual"))
        self.speed.setText(_translate("IHM", "Speed"))
        self.bluetooth.setText(_translate("IHM", "Bluetooth connection"))
        self.line.setText(_translate("IHM", "Line Follower state"))
        self.speed_limit.setText(_translate("IHM", "Under speed limit"))
        self.right.setText(_translate("IHM", "Right \n \n D"))
        self.stop.setText(_translate("IHM", "Emergency Stop"))
        self.left.setText(_translate("IHM", "Left \n \n Q"))
        self.backward.setText(_translate("IHM", "Backward \n \n S"))
        self.mode.setText(_translate("IHM", "Mode"))
        self.speed_mode.setText(_translate("IHM", "Speed Mode"))
        self.low_speed.setText(_translate("IHM", "Slow"))
        self.high_speed.setText(_translate("IHM", "Fast"))
        self.forward.setText(_translate("IHM", "Forward \n \n Z"))
        self.automatic.setText(_translate("IHM", "Automatic"))
        self.indicator.setText(_translate("IHM", "Light Indicator"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pilot_tab), _translate("IHM", "IHM Pilot"))
        self.down.setText(_translate("IHM", "Down \n \n M"))
        self.progressBar_2.setFormat(_translate("IHM", "%p"))
        self.manual_2.setText(_translate("IHM", "Manual"))
        self.speed_2.setText(_translate("IHM", "Speed"))
        self.right_2.setText(_translate("IHM", "Right \n \n D"))
        self.left_2.setText(_translate("IHM", "Left \n \n Q"))
        self.backward_2.setText(_translate("IHM", "Backward \n \n S"))
        self.mode_2.setText(_translate("IHM", "Mode"))
        self.forward_2.setText(_translate("IHM", "Forward \n \n Z"))
        self.up.setText(_translate("IHM", "Up \n \n P"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("IHM", "IHM Manu"))
        self.logo.setPixmap(QtGui.QPixmap("./images/logo500.png"))
        self.logo_2.setPixmap(QtGui.QPixmap("./images/logo500.png"))
        self.led_bluetooth.setPixmap(QtGui.QPixmap("./images/leds/red_led.png"))
        self.led_line.setPixmap(QtGui.QPixmap("./images/leds/white_led.png"))
        self.speed_limit_img.setPixmap(QtGui.QPixmap("./images/zone80.png"))
        self.led_speed.setPixmap(QtGui.QPixmap("./images/leds/green_led.png"))
        self.comboBox.setItemText(0, _translate("Dialog", "Color sensor"))
        self.comboBox.setItemText(1, _translate("Dialog", "Timer"))


