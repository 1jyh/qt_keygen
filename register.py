# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 544)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(610, 0, 191, 121))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 163, 21))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 163, 21))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.layoutWidget2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 70, 135, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(28, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 300, 541, 191))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 541, 171))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 151, 151))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_4)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(170, 10, 201, 151))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 190, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_3.setGeometry(QtCore.QRect(10, 10, 541, 271))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableView = QtWidgets.QTableView(self.tab_5)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 541, 251))
        self.tableView.setObjectName("tableView")
        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableView_2 = QtWidgets.QTableView(self.tab_6)
        self.tableView_2.setGeometry(QtCore.QRect(0, 0, 541, 251))
        self.tableView_2.setObjectName("tableView_2")
        self.tabWidget_3.addTab(self.tab_6, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 810, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuregister = QtWidgets.QMenu(self.menuBar)
        self.menuregister.setObjectName("menuregister")
        MainWindow.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menuregister.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.label.setText(_translate("MainWindow", "账号"))
        self.label_3.setText(_translate("MainWindow", "123"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "接码"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "打码"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "log"))
        self.label_4.setText(_translate("MainWindow", "邀请码"))
        self.label_6.setText(_translate("MainWindow", "线程数"))
        self.label_5.setText(_translate("MainWindow", "任务数"))
        self.label_7.setText(_translate("MainWindow", "接码id"))
        self.label_8.setText(_translate("MainWindow", "key"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "更多"))
        self.pushButton_2.setText(_translate("MainWindow", "start"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("MainWindow", "Tab 1"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("MainWindow", "Tab 2"))
        self.menuregister.setTitle(_translate("MainWindow", "register"))
