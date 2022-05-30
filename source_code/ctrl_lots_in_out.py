import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
import resources_rc
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QButtonGroup
import datetime
from lots_in_out import Ui_lots_in_out
from objects import In_Log, Out_Log
import sqlite3


class lots_in_out_window(QMainWindow, Ui_lots_in_out):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.main_window = self
        self.setWindowIcon(QIcon(":/images/image.ico"))
        QBG = QButtonGroup()
        QBG.addButton(self.in_radioButton)
        QBG.addButton(self.out_radioButton)
        self.generate_pushButton.clicked.connect(self.on_generate_btn_clicked)
        self.clear_lists_pushButton.clicked.connect(self.on_clear_btn_clicked)
        self.cancel_pushButton.clicked.connect(self.on_cancel_btn_clicked)
        self.confirm_pushButton.clicked.connect(self.on_confirm_btn_clicked)
        self.fill_table([])
        self.generate_pushButton.setStyleSheet("background:#BFCAE6")
        self.confirm_pushButton.setStyleSheet("background:#BFCAE6")
        self.in_radioButton.setStyleSheet("color:red")
        self.out_radioButton.setStyleSheet("color:green")
        self.in_radioButton.clicked.connect(self.on_in_radiobtn_clicked)
        self.out_radioButton.clicked.connect(self.on_out_radiobtn_clicked)

    def on_in_radiobtn_clicked(self):
        self.confirm_label.setText("入库操作")
        self.confirm_label.setStyleSheet("color:red")

    def on_out_radiobtn_clicked(self):
        self.confirm_label.setText("出库操作")
        self.confirm_label.setStyleSheet("color:green")

    def on_cancel_btn_clicked(self):
        self.close()

    def on_confirm_btn_clicked(self):
        if self.export_data == []:
            QMessageBox.question(self, '操作失败！', '出/入库详单中没有数据！', QMessageBox.Yes)
            return
        today_date = datetime.date.today()
        date_str = str(today_date.year * 10000 + today_date.month * 100 + today_date.day)
        # sql
        if self.in_radioButton.isChecked():  # 入库
            sql="insert into in_log values"
        else:
            sql

        if self.in_radioButton.isChecked():  # 入库

            for i in range(0, len(self.export_data)):
                in_obj = In_Log(date_str, self.export_data[i][0], self.export_data[i][1], self.export_data[i][2],
                                self.export_data[i][8], self.export_data[i][6], self.export_data[i][4],
                                self.export_data[i][9], self.export_data[i][10], self.export_data[i][11])
                in_obj.new_in_log()
                # 更新物料表结存数量
                conn = sqlite3.connect("material_management.db")
                conn.text_factory = str
                cur = conn.cursor()
                sql = "update material set now_num=" + str(
                    float(self.export_data[i][5]) + float(self.export_data[i][8])) + " where material_id='" + \
                      self.export_data[i][0] + "'"
                cur.execute(sql)
                conn.commit()
                cur.close()
                conn.close()
        else:  # 出库
            for i in range(0, len(self.export_data)):
                out_obj = Out_Log(date_str, self.export_data[i][0], self.export_data[i][1], self.export_data[i][2],
                                  self.export_data[i][8], self.export_data[i][6], self.export_data[i][4],
                                  self.export_data[i][9], self.export_data[i][10], self.export_data[i][11])
                out_obj.new_out_log()
                # 更新物料表结存数量
                conn = sqlite3.connect("material_management.db")
                conn.text_factory = str
                cur = conn.cursor()
                sql = "update material set now_num=" + str(
                    float(self.export_data[i][5]) - float(self.export_data[i][8])) + " where material_id='" + \
                      self.export_data[i][0] + "'"
                cur.execute(sql)
                conn.commit()
                cur.close()
                conn.close()

        QMessageBox.question(self, '入库成功！' if self.in_radioButton.isChecked() else '出库成功！', '批量操作完成！', QMessageBox.Yes)
        self.on_clear_btn_clicked()



    def fill_table(self, datas):  # datas为列表
        self.export_data = datas
        self.model = QStandardItemModel(len(datas), 11)
        self.model.setHorizontalHeaderLabels(
            ['存货编码', '存货名称', '规格型号', '计量单位', '库存位置', '结存数量', '单价(元)', '操作类型', '操作数量', '总价(元)', '使用人', "令号"])
        if datas != []:
            for i in range(0, len(datas)):
                item = QStandardItem(datas[i][0])
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 0, item)

                item = QStandardItem(datas[i][1])
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 1, item)

                item = QStandardItem(datas[i][2])
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 2, item)

                item = QStandardItem(datas[i][3])
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 3, item)

                item = QStandardItem(datas[i][4])
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 4, item)

                item = QStandardItem(format(float(datas[i][5]), '.4f'))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 5, item)

                item = QStandardItem(format(float(datas[i][6]), '.4f'))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 6, item)

                item = QStandardItem(datas[i][7])
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 7, item)

                item = QStandardItem(format(float(datas[i][8]), '.4f'))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 8, item)

                item = QStandardItem(format(float(datas[i][9]), '.4f'))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 9, item)

                item = QStandardItem(datas[i][10])
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 10, item)

                item = QStandardItem(datas[i][11])
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 11, item)

        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()
        self.tableView.resizeRowsToContents()
        self.tableView.horizontalHeader().setStretchLastSection(True)

    def on_clear_btn_clicked(self):
        self.id_textEdit.setPlainText("")
        self.num_textEdit.setPlainText("")
        self.user_textEdit.setPlainText("")
        self.code_textEdit.setPlainText("")
        self.in_radioButton.setChecked(False)
        self.out_radioButton.setChecked(False)
        self.fill_table([])

    def on_generate_btn_clicked(self):
        if self.in_radioButton.isChecked():
            all_in_flag = 1
        elif self.out_radioButton.isChecked():
            all_in_flag = 0
        else:
            QMessageBox.question(self, '生成失败！', '请选择入库还是出库！', QMessageBox.Yes)
            return
        id_str = self.id_textEdit.toPlainText()
        id_str = id_str.strip('\n\t ')
        if id_str == "":
            QMessageBox.question(self, '生成失败！', '存货编码不可为空！', QMessageBox.Yes)
            return

        id_ll = id_str.split('\n')
        id_len = len(id_ll)
        for i in range(0, id_len):
            id_ll[i] = id_ll[i].strip('\n\t ')
        # 判断重复
        for i in range(0, id_len):
            for j in range(i + 1, id_len):
                if id_ll[i] == id_ll[j]:
                    QMessageBox.question(self, '生成失败！', '存货编码列表第' + str(i + 1) + "行与第" + str(j + 1) + "行重复！\n请自行合并！",
                                         QMessageBox.Yes)
                    return

        num_str = self.num_textEdit.toPlainText()
        if num_str == "":
            QMessageBox.question(self, '生成失败！', '操作数量不可为空！', QMessageBox.Yes)
            return
        else:
            num_str = num_str.strip('\n\t ')
            num_ll = num_str.split('\n')

            if len(num_ll) != id_len:
                QMessageBox.question(self, '生成失败！', '操作数量列表条数与存货编码列表不一致！', QMessageBox.Yes)
                return
            for i in range(0, id_len):
                num_ll[i] = num_ll[i].strip('\n\t ')

        user_str = self.user_textEdit.toPlainText()
        if user_str == "":
            QMessageBox.question(self, '生成失败！', '使用人不可为空！', QMessageBox.Yes)
            return
        else:
            user_str = user_str.strip('\n\t ')
            user_ll = user_str.split('\n')
            if len(user_ll) != id_len:
                QMessageBox.question(self, '生成失败！', '使用人列表条数与存货编码列表不一致！', QMessageBox.Yes)
                return
            for i in range(0, id_len):
                user_ll[i] = user_ll[i].strip('\n\t ')

        code_str = self.code_textEdit.toPlainText()
        if code_str == "":
            QMessageBox.question(self, '生成失败！', '令号不可为空！', QMessageBox.Yes)
            return
        else:
            code_str = code_str.strip('\n\t ')
            code_ll = code_str.split('\n')
            if len(code_ll) != id_len:
                QMessageBox.question(self, '生成失败！', '令号列表条数与存货编码列表不一致！', QMessageBox.Yes)
                return
            for i in range(0, id_len):
                code_ll[i] = code_ll[i].strip('\n\t ')

        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        table_data = []
        for i in range(0, id_len):
            sql = "select material_name,spec,unit,pos,now_num,per_price from material where material_id='" + id_ll[
                i] + "'"
            try:
                cur.execute(sql)
            except:
                QMessageBox.question(self, '生成失败！', '第' + str(i + 1) + "条存货编码不存在！\n所有存货均未进行出、入库操作！", QMessageBox.Yes)
                cur.close()
                conn.close()
                return
            res = cur.fetchone()
            if res is None:
                QMessageBox.question(self, '生成失败！', '第' + str(i + 1) + "条存货编码不存在！\n所有存货均未进行出、入库操作！", QMessageBox.Yes)
                cur.close()
                conn.close()
                return
            tmp = []
            tmp.append(id_ll[i])
            tmp.append(res[0])
            tmp.append(res[1])
            tmp.append(res[2])
            tmp.append(res[3])
            tmp.append(str(res[4]))
            tmp.append(str(res[5]))
            if all_in_flag:
                tmp.append('入库')
            else:
                tmp.append('出库')
            try:
                tt = float(num_ll[i])
            except:
                QMessageBox.question(self, '生成失败！', '第' + str(i + 1) + "条操作数量不是实数！\n所有存货均未进行出、入库操作！", QMessageBox.Yes)
                cur.close()
                conn.close()
                return
            if all_in_flag == 0 and tt > res[4]:
                QMessageBox.question(self, '生成失败！', '第' + str(i + 1) + "条存货的出库数量大于现有库存！\n所有存货均未进行出、入库操作！", QMessageBox.Yes)
                cur.close()
                conn.close()
                return
            tmp.append(num_ll[i])
            tmp.append(str(res[5] * tt))  # 总价
            tmp.append(user_ll[i])
            tmp.append(code_ll[i])
            table_data.append(tmp)
        cur.close()
        conn.close()
        self.fill_table(table_data)
        QMessageBox.question(self, '生成成功！', "详单已填充至下方表格，请仔细核查！", QMessageBox.Yes)
