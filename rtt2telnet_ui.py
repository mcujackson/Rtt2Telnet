# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rtt2telnet.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(273, 208)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.chipCombox = QtWidgets.QComboBox(self.centralwidget)
        self.chipCombox.setObjectName("chipCombox")
        self.horizontalLayout.addWidget(self.chipCombox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.interfaceCombox = QtWidgets.QComboBox(self.centralwidget)
        self.interfaceCombox.setObjectName("interfaceCombox")
        self.interfaceCombox.addItem("")
        self.interfaceCombox.addItem("")
        self.interfaceCombox.addItem("")
        self.interfaceCombox.addItem("")
        self.horizontalLayout_2.addWidget(self.interfaceCombox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.speedCombox = QtWidgets.QComboBox(self.centralwidget)
        self.speedCombox.setObjectName("speedCombox")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.speedCombox.addItem("")
        self.horizontalLayout_3.addWidget(self.speedCombox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.channel0Port = QtWidgets.QLineEdit(self.centralwidget)
        self.channel0Port.setObjectName("channel0Port")
        self.horizontalLayout_4.addWidget(self.channel0Port)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.channel1Port = QtWidgets.QLineEdit(self.centralwidget)
        self.channel1Port.setObjectName("channel1Port")
        self.horizontalLayout_5.addWidget(self.channel1Port)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.switchButton = QtWidgets.QPushButton(self.centralwidget)
        self.switchButton.setObjectName("switchButton")
        self.horizontalLayout_6.addWidget(self.switchButton)
        self.hideButton = QtWidgets.QPushButton(self.centralwidget)
        self.hideButton.setObjectName("hideButton")
        self.horizontalLayout_6.addWidget(self.hideButton)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 273, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menu)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.action619808090_qq_com = QtWidgets.QAction(MainWindow)
        self.action619808090_qq_com.setObjectName("action619808090_qq_com")
        self.actionDriver = QtWidgets.QAction(MainWindow)
        self.actionDriver.setObjectName("actionDriver")
        self.menu_2.addAction(self.action619808090_qq_com)
        self.menu_3.addAction(self.actionDriver)
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.speedCombox.setCurrentIndex(20)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RTT转Telnet工具"))
        self.label.setText(_translate("MainWindow", "芯片型号:"))
        self.label_2.setText(_translate("MainWindow", "目标接口:"))
        self.interfaceCombox.setItemText(0, _translate("MainWindow", "SWD"))
        self.interfaceCombox.setItemText(1, _translate("MainWindow", "JTAG"))
        self.interfaceCombox.setItemText(2, _translate("MainWindow", "cJTAG"))
        self.interfaceCombox.setItemText(3, _translate("MainWindow", "FINE"))
        self.label_3.setText(_translate("MainWindow", "速度:"))
        self.speedCombox.setItemText(0, _translate("MainWindow", "5kHz"))
        self.speedCombox.setItemText(1, _translate("MainWindow", "10kHz"))
        self.speedCombox.setItemText(2, _translate("MainWindow", "20kHz"))
        self.speedCombox.setItemText(3, _translate("MainWindow", "30kHz"))
        self.speedCombox.setItemText(4, _translate("MainWindow", "50kHz"))
        self.speedCombox.setItemText(5, _translate("MainWindow", "100kHz"))
        self.speedCombox.setItemText(6, _translate("MainWindow", "200kHz"))
        self.speedCombox.setItemText(7, _translate("MainWindow", "300kHz"))
        self.speedCombox.setItemText(8, _translate("MainWindow", "400kHz"))
        self.speedCombox.setItemText(9, _translate("MainWindow", "500kHz"))
        self.speedCombox.setItemText(10, _translate("MainWindow", "600kHz"))
        self.speedCombox.setItemText(11, _translate("MainWindow", "650kHz"))
        self.speedCombox.setItemText(12, _translate("MainWindow", "750kHz"))
        self.speedCombox.setItemText(13, _translate("MainWindow", "900kHz"))
        self.speedCombox.setItemText(14, _translate("MainWindow", "1000kHz"))
        self.speedCombox.setItemText(15, _translate("MainWindow", "1334kHz"))
        self.speedCombox.setItemText(16, _translate("MainWindow", "1600kHz"))
        self.speedCombox.setItemText(17, _translate("MainWindow", "2000kHz"))
        self.speedCombox.setItemText(18, _translate("MainWindow", "2667kHz"))
        self.speedCombox.setItemText(19, _translate("MainWindow", "3200kHz"))
        self.speedCombox.setItemText(20, _translate("MainWindow", "4000kHz"))
        self.speedCombox.setItemText(21, _translate("MainWindow", "4800kHz"))
        self.speedCombox.setItemText(22, _translate("MainWindow", "5334kHz"))
        self.speedCombox.setItemText(23, _translate("MainWindow", "6000kHz"))
        self.speedCombox.setItemText(24, _translate("MainWindow", "8000kHz"))
        self.speedCombox.setItemText(25, _translate("MainWindow", "9600kHz"))
        self.speedCombox.setItemText(26, _translate("MainWindow", "12000kHz"))
        self.label_4.setText(_translate("MainWindow", "通道0对应端口号:"))
        self.channel0Port.setText(_translate("MainWindow", "6198"))
        self.label_5.setText(_translate("MainWindow", "通道1对应端口号:"))
        self.channel1Port.setText(_translate("MainWindow", "6199"))
        self.switchButton.setText(_translate("MainWindow", "开启"))
        self.hideButton.setText(_translate("MainWindow", "隐入托盘"))
        self.menu.setTitle(_translate("MainWindow", "作者"))
        self.menu_2.setTitle(_translate("MainWindow", "邮箱"))
        self.menu_3.setTitle(_translate("MainWindow", "姓名"))
        self.action619808090_qq_com.setText(_translate("MainWindow", "619808090@qq.com"))
        self.actionDriver.setText(_translate("MainWindow", "Driver"))
