# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 500)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setItalic(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(5, 0, 20);\n"
"color: rgb(175, 181, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(218, 22, 234, 33))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.dragAndDrop = QtWidgets.QWidget(self.centralwidget)
        self.dragAndDrop.setGeometry(QtCore.QRect(10, 70, 650, 240))
        self.dragAndDrop.setMouseTracking(True)
        self.dragAndDrop.setAcceptDrops(True)
        self.dragAndDrop.setStyleSheet("border-color: rgb(151, 250, 255);\n"
"background-color: rgb(8, 0, 35);")
        self.dragAndDrop.setObjectName("dragAndDrop")
        self.button_ok = QtWidgets.QPushButton(self.centralwidget)
        self.button_ok.setGeometry(QtCore.QRect(10, 313, 561, 38))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setItalic(False)
        self.button_ok.setFont(font)
        self.button_ok.setStyleSheet("color: rgb(154, 181, 255);\n"
"border-color: rgb(0, 1, 77);")
        self.button_ok.setObjectName("button_ok")
        self.listing_view = QtWidgets.QListView(self.centralwidget)
        self.listing_view.setGeometry(QtCore.QRect(10, 360, 651, 131))
        self.listing_view.setObjectName("listing_view")
        self.listing = QtWidgets.QListWidget(self.centralwidget)
        self.listing.setGeometry(QtCore.QRect(10, 360, 651, 131))
        self.listing.setObjectName("listing")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(579, 313, 83, 38))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.reset.setFont(font)
        self.reset.setStyleSheet("color: rgb(154, 181, 255);\n"
"border-color: rgb(0, 1, 77);")
        self.reset.setObjectName("reset")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Drag and drop files or folder"))
        self.button_ok.setText(_translate("MainWindow", "OK"))
        self.reset.setText(_translate("MainWindow", "Reset"))
