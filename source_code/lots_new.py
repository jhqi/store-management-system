# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lots_new.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_lots_new(object):
    def setupUi(self, lots_new):
        lots_new.setObjectName("lots_new")
        lots_new.resize(1260, 700)
        self.id_textEdit = QtWidgets.QPlainTextEdit(lots_new)
        self.id_textEdit.setGeometry(QtCore.QRect(10, 30, 131, 251))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.id_textEdit.setFont(font)
        self.id_textEdit.setObjectName("id_textEdit")
        self.label = QtWidgets.QLabel(lots_new)
        self.label.setGeometry(QtCore.QRect(10, 0, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableView = QtWidgets.QTableView(lots_new)
        self.tableView.setGeometry(QtCore.QRect(10, 340, 951, 351))
        self.tableView.setObjectName("tableView")
        self.textEdit = QtWidgets.QTextEdit(lots_new)
        self.textEdit.setGeometry(QtCore.QRect(1090, 10, 161, 631))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.confirm_pushButton = QtWidgets.QPushButton(lots_new)
        self.confirm_pushButton.setGeometry(QtCore.QRect(1090, 650, 71, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_pushButton.setFont(font)
        self.confirm_pushButton.setObjectName("confirm_pushButton")
        self.cancel_pushButton = QtWidgets.QPushButton(lots_new)
        self.cancel_pushButton.setGeometry(QtCore.QRect(1180, 650, 71, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_pushButton.setFont(font)
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.label_4 = QtWidgets.QLabel(lots_new)
        self.label_4.setGeometry(QtCore.QRect(160, 0, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.name_textEdit = QtWidgets.QPlainTextEdit(lots_new)
        self.name_textEdit.setGeometry(QtCore.QRect(160, 30, 131, 251))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.name_textEdit.setFont(font)
        self.name_textEdit.setObjectName("name_textEdit")
        self.spec_textEdit = QtWidgets.QPlainTextEdit(lots_new)
        self.spec_textEdit.setGeometry(QtCore.QRect(310, 30, 131, 251))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.spec_textEdit.setFont(font)
        self.spec_textEdit.setObjectName("spec_textEdit")
        self.unit_textEdit = QtWidgets.QPlainTextEdit(lots_new)
        self.unit_textEdit.setGeometry(QtCore.QRect(460, 30, 131, 251))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.unit_textEdit.setFont(font)
        self.unit_textEdit.setObjectName("unit_textEdit")
        self.label_5 = QtWidgets.QLabel(lots_new)
        self.label_5.setGeometry(QtCore.QRect(310, 0, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(lots_new)
        self.label_6.setGeometry(QtCore.QRect(460, 0, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.generate_pushButton = QtWidgets.QPushButton(lots_new)
        self.generate_pushButton.setGeometry(QtCore.QRect(970, 290, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.generate_pushButton.setFont(font)
        self.generate_pushButton.setObjectName("generate_pushButton")
        self.label_3 = QtWidgets.QLabel(lots_new)
        self.label_3.setGeometry(QtCore.QRect(10, 300, 141, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ori_num_textEdit = QtWidgets.QPlainTextEdit(lots_new)
        self.ori_num_textEdit.setGeometry(QtCore.QRect(610, 30, 131, 251))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.ori_num_textEdit.setFont(font)
        self.ori_num_textEdit.setObjectName("ori_num_textEdit")
        self.label_7 = QtWidgets.QLabel(lots_new)
        self.label_7.setGeometry(QtCore.QRect(610, 0, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pos_textEdit = QtWidgets.QPlainTextEdit(lots_new)
        self.pos_textEdit.setGeometry(QtCore.QRect(760, 30, 131, 251))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.pos_textEdit.setFont(font)
        self.pos_textEdit.setObjectName("pos_textEdit")
        self.label_8 = QtWidgets.QLabel(lots_new)
        self.label_8.setGeometry(QtCore.QRect(760, 0, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.price_textEdit = QtWidgets.QPlainTextEdit(lots_new)
        self.price_textEdit.setGeometry(QtCore.QRect(910, 30, 131, 251))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.price_textEdit.setFont(font)
        self.price_textEdit.setObjectName("price_textEdit")
        self.label_9 = QtWidgets.QLabel(lots_new)
        self.label_9.setGeometry(QtCore.QRect(910, 0, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.clear_lists_pushButton = QtWidgets.QPushButton(lots_new)
        self.clear_lists_pushButton.setGeometry(QtCore.QRect(970, 350, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.clear_lists_pushButton.setFont(font)
        self.clear_lists_pushButton.setObjectName("clear_lists_pushButton")

        self.retranslateUi(lots_new)
        QtCore.QMetaObject.connectSlotsByName(lots_new)

    def retranslateUi(self, lots_new):
        _translate = QtCore.QCoreApplication.translate
        lots_new.setWindowTitle(_translate("lots_new", "批量新增存货"))
        self.label.setText(_translate("lots_new", "存货编码："))
        self.textEdit.setHtml(_translate("lots_new", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">使用说明：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">1.上方7个列表均支持从</span><span style=\" font-family:\'SimSun\'; color:#0000ff;\">Excel文件</span><span style=\" font-family:\'SimSun\';\">中复制</span><span style=\" font-family:\'SimSun\'; color:#0000ff;\">一列</span><span style=\" font-family:\'SimSun\';\">数据后粘贴。即每条记录的某项属性，均在</span><span style=\" font-family:\'SimSun\'; color:#0000ff;\">相应的列表中占1行</span><span style=\" font-family:\'SimSun\';\">；</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">2.上方列表</span><span style=\" font-family:\'SimSun\'; color:#0000ff;\">不可为空，</span><span style=\" font-family:\'SimSun\'; color:#000000;\">且</span><span style=\" font-family:\'SimSun\'; color:#0000ff;\">行数</span><span style=\" font-family:\'SimSun\'; color:#000000;\">要求</span><span style=\" font-family:\'SimSun\'; color:#0000ff;\">相同；</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; color:#000000;\">3.填充列表后，按</span><span style=\" font-family:\'SimSun\'; color:#0000ff;\">“生成”按钮</span><span style=\" font-family:\'SimSun\'; color:#000000;\">，自动生成“新增存货详单”；</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; color:#000000;\">4.核查后，点击确定，完成批量新增操作。</span></p></body></html>"))
        self.confirm_pushButton.setText(_translate("lots_new", "确认"))
        self.cancel_pushButton.setText(_translate("lots_new", "关闭"))
        self.label_4.setText(_translate("lots_new", "存货名称："))
        self.label_5.setText(_translate("lots_new", "规格型号："))
        self.label_6.setText(_translate("lots_new", "计量单位："))
        self.generate_pushButton.setText(_translate("lots_new", "生成详单"))
        self.label_3.setText(_translate("lots_new", "新增存货详单："))
        self.label_7.setText(_translate("lots_new", "期初数量："))
        self.label_8.setText(_translate("lots_new", "库存位置："))
        self.label_9.setText(_translate("lots_new", "单价(元)："))
        self.clear_lists_pushButton.setText(_translate("lots_new", "清空列表"))
