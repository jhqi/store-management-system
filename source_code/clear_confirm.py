# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clear_confirm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_clear_confirm(object):
    def setupUi(self, clear_confirm):
        clear_confirm.setObjectName("clear_confirm")
        clear_confirm.resize(410, 234)
        self.label = QtWidgets.QLabel(clear_confirm)
        self.label.setGeometry(QtCore.QRect(20, 30, 371, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.confirm_btn = QtWidgets.QPushButton(clear_confirm)
        self.confirm_btn.setGeometry(QtCore.QRect(90, 170, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_btn.setFont(font)
        self.confirm_btn.setObjectName("confirm_btn")
        self.cancel_btn = QtWidgets.QPushButton(clear_confirm)
        self.cancel_btn.setGeometry(QtCore.QRect(240, 170, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName("cancel_btn")
        self.label_2 = QtWidgets.QLabel(clear_confirm)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 241, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(clear_confirm)
        QtCore.QMetaObject.connectSlotsByName(clear_confirm)

    def retranslateUi(self, clear_confirm):
        _translate = QtCore.QCoreApplication.translate
        clear_confirm.setWindowTitle(_translate("clear_confirm", "确认清空"))
        self.label.setText(_translate("clear_confirm", "警告！  确认清空该项数据？？"))
        self.confirm_btn.setText(_translate("clear_confirm", "确认"))
        self.cancel_btn.setText(_translate("clear_confirm", "取消"))
        self.label_2.setText(_translate("clear_confirm", "TextLabel"))

