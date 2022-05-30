# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import_confirm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_import_confirm(object):
    def setupUi(self, import_confirm):
        import_confirm.setObjectName("import_confirm")
        import_confirm.resize(470, 234)
        self.label = QtWidgets.QLabel(import_confirm)
        self.label.setGeometry(QtCore.QRect(20, 30, 431, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.confirm_btn = QtWidgets.QPushButton(import_confirm)
        self.confirm_btn.setGeometry(QtCore.QRect(110, 170, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_btn.setFont(font)
        self.confirm_btn.setObjectName("confirm_btn")
        self.cancel_btn = QtWidgets.QPushButton(import_confirm)
        self.cancel_btn.setGeometry(QtCore.QRect(270, 170, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName("cancel_btn")
        self.label_2 = QtWidgets.QLabel(import_confirm)
        self.label_2.setGeometry(QtCore.QRect(80, 100, 311, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(import_confirm)
        QtCore.QMetaObject.connectSlotsByName(import_confirm)

    def retranslateUi(self, import_confirm):
        _translate = QtCore.QCoreApplication.translate
        import_confirm.setWindowTitle(_translate("import_confirm", "确认导入"))
        self.label.setText(_translate("import_confirm", "11"))
        self.confirm_btn.setText(_translate("import_confirm", "确认"))
        self.cancel_btn.setText(_translate("import_confirm", "取消"))
        self.label_2.setText(_translate("import_confirm", "TextLabel"))

