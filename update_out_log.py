# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_out_log.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_update_out_log(object):
    def setupUi(self, update_out_log):
        update_out_log.setObjectName("update_out_log")
        update_out_log.resize(660, 500)
        self.verticalLayoutWidget = QtWidgets.QWidget(update_out_log)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 379, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_2.addWidget(self.dateEdit)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.material_id_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.material_id_lineEdit.setFont(font)
        self.material_id_lineEdit.setObjectName("material_id_lineEdit")
        self.horizontalLayout_6.addWidget(self.material_id_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.material_name_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.material_name_lineEdit.setFont(font)
        self.material_name_lineEdit.setText("")
        self.material_name_lineEdit.setObjectName("material_name_lineEdit")
        self.horizontalLayout_5.addWidget(self.material_name_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.spec_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.spec_lineEdit.setFont(font)
        self.spec_lineEdit.setObjectName("spec_lineEdit")
        self.horizontalLayout_4.addWidget(self.spec_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.per_price_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.per_price_lineEdit.setFont(font)
        self.per_price_lineEdit.setObjectName("per_price_lineEdit")
        self.horizontalLayout_9.addWidget(self.per_price_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.position_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.position_lineEdit.setFont(font)
        self.position_lineEdit.setObjectName("position_lineEdit")
        self.horizontalLayout_10.addWidget(self.position_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.num_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.num_lineEdit.setFont(font)
        self.num_lineEdit.setObjectName("num_lineEdit")
        self.horizontalLayout.addWidget(self.num_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.user_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.user_lineEdit.setFont(font)
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.horizontalLayout_7.addWidget(self.user_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.agree_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.agree_lineEdit.setFont(font)
        self.agree_lineEdit.setObjectName("agree_lineEdit")
        self.horizontalLayout_8.addWidget(self.agree_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.cancel_pushButton = QtWidgets.QPushButton(update_out_log)
        self.cancel_pushButton.setGeometry(QtCore.QRect(470, 270, 141, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_pushButton.setFont(font)
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.both_btn = QtWidgets.QPushButton(update_out_log)
        self.both_btn.setGeometry(QtCore.QRect(420, 170, 231, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.both_btn.setFont(font)
        self.both_btn.setObjectName("both_btn")

        self.retranslateUi(update_out_log)
        QtCore.QMetaObject.connectSlotsByName(update_out_log)

    def retranslateUi(self, update_out_log):
        _translate = QtCore.QCoreApplication.translate
        update_out_log.setWindowTitle(_translate("update_out_log", "确认修改出库记录"))
        self.label_6.setText(_translate("update_out_log", "出库日期："))
        self.label_2.setText(_translate("update_out_log", "存货编码："))
        self.label_3.setText(_translate("update_out_log", "存货名称："))
        self.label.setText(_translate("update_out_log", "规格型号："))
        self.label_9.setText(_translate("update_out_log", "单价(元)："))
        self.label_10.setText(_translate("update_out_log", "库存位置："))
        self.label_4.setText(_translate("update_out_log", "操作类型："))
        self.comboBox.setItemText(0, _translate("update_out_log", "入库"))
        self.comboBox.setItemText(1, _translate("update_out_log", "出库"))
        self.label_5.setText(_translate("update_out_log", "操作数量："))
        self.label_7.setText(_translate("update_out_log", "使用人员："))
        self.label_8.setText(_translate("update_out_log", "令号："))
        self.cancel_pushButton.setText(_translate("update_out_log", "取消"))
        self.both_btn.setText(_translate("update_out_log", "修改出库记录和结存数量"))
