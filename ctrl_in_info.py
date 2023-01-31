import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
import resources_rc
import sqlite3
import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QInputDialog, QHeaderView
from openpyxl import Workbook
from in_info import Ui_in_info
from ctrl_update_in_log import update_in_log_window
import var
import datetime


class in_info_window(QMainWindow, Ui_in_info):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.main_window = self
        self.setWindowIcon(QIcon(":/images/image.ico"))
        self.query_btn.setStyleSheet("background:#FF95CA")
        self.st_dateEdit.setDate(QDate(2000, 1, 1))
        self.ed_dateEdit.setDate(QDate(2050, 12, 31))
        self.selected_row = -1
        self.export_data = []
        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        sql = "select * from in_log"
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        conn.close()
        self.fill_table(res)
        self.query_btn.clicked.disconnect()
        self.del_btn.clicked.disconnect()
        self.update_btn.clicked.disconnect()

        self.query_btn.clicked.connect(self.on_query_btn_clicked)
        self.clear_query_btn.clicked.connect(self.on_clear_query_btn_clicked)
        self.del_btn.clicked.connect(self.on_del_btn_clicked)
        self.update_btn.clicked.connect(self.on_update_btn_clicked)
        self.cancel_btn.clicked.connect(self.on_cancel_btn_clicked)
        self.tableView.clicked.connect(self.on_tableview_select_item)
        self.export_excel.clicked.connect(self.on_export_btn_clicked)

    def on_export_btn_clicked(self):
        if self.export_data == []:
            QMessageBox.question(self, '导出失败！', '请确认表中存在入库数据！', QMessageBox.Yes)
            return
        book = Workbook()
        sheet = book.active
        sheet.append(('日期', '存货编码', '存货名称', '规格型号', '收入数量', '单价(元)', '库存位置', '总价(元)', '使用人', '令号'))
        for i in range(len(self.export_data)):
            tdate_year = self.export_data[i][0] // 10000
            tdate_month = self.export_data[i][0] % 10000 // 100
            tdate_day = self.export_data[i][0] % 100
            tdate = datetime.date(tdate_year, tdate_month, tdate_day)
            if self.export_data[i][5] == -1:
                per_price = '未知'
            else:
                per_price = self.export_data[i][5]

            if self.export_data[i][7] == -1:
                total_price = '未知'
            else:
                total_price = self.export_data[i][7]
            tmp = (
            tdate, self.export_data[i][1], self.export_data[i][2], self.export_data[i][3], self.export_data[i][4],
            per_price, self.export_data[i][6], total_price, self.export_data[i][8], self.export_data[i][9])
            sheet.append(tmp)

        tmp_dialog = QtWidgets.QFileDialog(None, "选取入库数据保存路径", "C:/")
        tmp_dialog.setLabelText(QtWidgets.QFileDialog.Accept, '确认')
        tmp_dialog.setLabelText(QtWidgets.QFileDialog.Reject, '取消')
        tmp_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        if tmp_dialog.exec_():
            ll = tmp_dialog.selectedFiles()
            dir_path = ll[0]
        else:
            return
        time_str = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        file_name = time_str + "入库数据.xlsx"
        content, conform = QInputDialog.getText(self.main_window, '文件名', '请输入文件名：', text=file_name)
        if conform:
            file_name = content
        else:
            return
        try:
            book.save(dir_path + "/" + file_name)
            QMessageBox.question(self, '导出成功！', '入库数据已导出至Excel！', QMessageBox.Yes)
        except:
            QMessageBox.question(self, '导出失败！', '文件名有误！', QMessageBox.Yes)

    def on_tableview_select_item(self, event):
        self.selected_row = self.tableView.currentIndex().row()
        # self.tableView.selectRow(self.selected_row)

    def fill_table(self, datas):  # datas为列表
        self.export_data = datas
        self.model = QStandardItemModel(len(datas), 10)
        self.model.setHorizontalHeaderLabels(
            ['日期', '存货编码', '存货名称', '规格型号', '收入数量', '单价(元)', '库存位置', '总价(元)', '使用人', '令号'])
        if datas != []:
            for i in range(0, len(datas)):
                tdate_year = datas[i][0] // 10000
                tdate_month = datas[i][0] % 10000 // 100
                tdate_day = datas[i][0] % 100
                tdate = str(tdate_year) + "-" + str(tdate_month) + "-" + str(tdate_day)
                item = QStandardItem(tdate)
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

                item = QStandardItem(format(datas[i][4], '.2f'))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 4, item)

                t_per_price = datas[i][5]
                if t_per_price == -1:
                    t_per_price = '未知'
                else:
                    t_per_price = format(t_per_price, '.2f')

                item = QStandardItem(t_per_price)
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 5, item)

                item = QStandardItem(datas[i][6])
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 6, item)

                t_total_price = datas[i][7]
                if t_total_price == -1:
                    t_total_price = '未知'
                else:
                    t_total_price = format(t_total_price, '.2f')

                item = QStandardItem(t_total_price)
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 7, item)

                item = QStandardItem(datas[i][8])
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 8, item)

                item = QStandardItem(datas[i][9])
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 9, item)

        self.tableView.setModel(self.model)
        # self.tableView.resizeColumnsToContents()
        self.tableView.resizeRowsToContents()
        # self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        self.tableView.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)
        self.tableView.horizontalHeader().setSectionResizeMode(3, QHeaderView.Interactive)
        self.tableView.horizontalHeader().setSectionResizeMode(4, QHeaderView.Interactive)
        self.tableView.horizontalHeader().setSectionResizeMode(5, QHeaderView.Interactive)
        self.tableView.horizontalHeader().setSectionResizeMode(6, QHeaderView.Interactive)
        self.tableView.horizontalHeader().setSectionResizeMode(7, QHeaderView.Interactive)
        self.tableView.horizontalHeader().setSectionResizeMode(8, QHeaderView.Interactive)
        self.tableView.horizontalHeader().setSectionResizeMode(9, QHeaderView.Interactive)
        self.tableView.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)

    def my_query(self):
        if self.st_num.text() == "":
            st_num = "0"
        else:
            st_num = self.st_num.text()
        if self.ed_num.text() == "":
            ed_num = "999999999"
        else:
            ed_num = self.ed_num.text()
        try:
            t1 = float(st_num)
            t2 = float(ed_num)
        except:
            return (0, [])
        if t1 > t2:
            return (1, [])
        st_date = self.st_dateEdit.date().toString(Qt.ISODate)
        ll = st_date.split('-')
        st_date = "".join(ll)

        ed_date = self.ed_dateEdit.date().toString(Qt.ISODate)
        ll = ed_date.split('-')
        ed_date = "".join(ll)

        if int(st_date) > int(ed_date):
            return (2, [])
        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        sql = "select * from in_log where (in_num between " + st_num + " and " + ed_num + " ) and  (date_time between " + st_date + " and " + ed_date + " ) "

        if self.id.text() != "":
            id_str = self.id.text()
            id_str = id_str.strip('%\n\t ')
            id_ll = id_str.split('%')
            sql += " and ("
            for i in range(len(id_ll)):
                sql += "material_id='" + id_ll[i] + "'"
                if i < len(id_ll) - 1:
                    sql += " or "
            sql += ")"

        if self.name.text() != "":
            name_str = self.name.text()
            name_str = name_str.strip('%\n\t ')
            name_ll = name_str.split('%')
            name_ll1 = []
            name_ll2 = []
            for tname in name_ll:
                name_ll1.append("%" + tname + "%")
                name_ll2.append("%%" + tname + "%%")
            sql += " and ("
            for i in range(len(name_ll)):
                sql += "material_name like '" + name_ll1[i] + "' or material_name like '" + name_ll2[i] + "'"
                if i < len(name_ll) - 1:
                    sql += " or "
            sql += ")"

        if self.spec_lineEdit.text() != "":
            name_str = self.spec_lineEdit.text()
            name_str = name_str.strip('%\n\t ')
            name_ll = name_str.split('%')
            name_ll1 = []
            name_ll2 = []
            for tname in name_ll:
                name_ll1.append("%" + tname + "%")
                name_ll2.append("%%" + tname + "%%")
            sql += " and ("
            for i in range(len(name_ll)):
                sql += "spec like '" + name_ll1[i] + "' or spec like '" + name_ll2[i] + "'"
                if i < len(name_ll) - 1:
                    sql += " or "
            sql += ")"

        if self.user_lineEdit.text() != "":
            name_str = self.user_lineEdit.text()
            name_str = name_str.strip('%\n\t ')
            name_ll = name_str.split('%')
            name_ll1 = []
            name_ll2 = []
            for tname in name_ll:
                name_ll1.append("%" + tname + "%")
                name_ll2.append("%%" + tname + "%%")
            sql += " and ("
            for i in range(len(name_ll)):
                sql += "user_man like '" + name_ll1[i] + "' or user_man like '" + name_ll2[i] + "'"
                if i < len(name_ll) - 1:
                    sql += " or "
            sql += ")"

        if self.agree_lineEdit.text() != "":
            name_str = self.agree_lineEdit.text()
            name_str = name_str.strip('%\n\t ')
            name_ll = name_str.split('%')
            name_ll1 = []
            name_ll2 = []
            for tname in name_ll:
                name_ll1.append("%" + tname + "%")
                name_ll2.append("%%" + tname + "%%")
            sql += " and ("
            for i in range(len(name_ll)):
                sql += "agree_man like '" + name_ll1[i] + "' or agree_man like '" + name_ll2[i] + "'"
                if i < len(name_ll) - 1:
                    sql += " or "
            sql += ")"

        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        conn.close()
        if res == []:
            return (3, [])
        return (4, res)

    def on_query_btn_clicked(self):
        (flag, res) = self.my_query()
        if flag == 0:
            QMessageBox.question(self, '查询失败！', '入库数量范围应输入实数！', QMessageBox.Yes)
            self.fill_table([])
            return
        elif flag == 1:
            QMessageBox.question(self, '查询失败！', '入库数量范围冲突！', QMessageBox.Yes)
            self.fill_table([])
            return
        elif flag == 2:
            QMessageBox.question(self, '查询失败！', '入库日期范围冲突！', QMessageBox.Yes)
            self.fill_table([])
            return
        elif flag == 3:
            QMessageBox.question(self, '查询失败！', '未查询到相关入库信息！', QMessageBox.Yes)
            self.fill_table([])
            return
        else:
            self.fill_table(res)
            QMessageBox.question(self, '查询成功！', '相关入库记录已列在表中！', QMessageBox.Yes)

    def on_tableview_select_item(self, event):
        self.selected_row = self.tableView.currentIndex().row()
        # self.tableView.selectRow(self.selected_row)

    def on_del_btn_clicked(self):
        indexs = self.tableView.selectionModel().selectedIndexes()
        tt = set()
        for t in indexs:
            tt.add(t.row())
        indexs = []
        for t in tt:
            indexs.append(t)
        if indexs == []:
            QMessageBox.question(self, '删除失败！', '请正确选择入库记录！', QMessageBox.Yes)
            return
        id_ll = []
        num_ll = []
        material_id_ll = []
        for index in indexs:
            row_num = index
            tlog_id = str(self.export_data[row_num][10])
            id_ll.append(tlog_id)
            t_in_num = self.export_data[row_num][4]
            num_ll.append(t_in_num)
            t_material_id = self.export_data[row_num][1]
            material_id_ll.append(t_material_id)

        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        for i in range(0, len(id_ll)):
            sql = "select now_num from material where material_id='" + material_id_ll[i] + "'"
            cur.execute(sql)
            res = cur.fetchone()
            now_num = res[0]
            new_num = now_num - num_ll[i]
            if new_num < 0:
                if len(id_ll) == 1:
                    QMessageBox.question(self, '删除失败！', '若删除该条入库记录，对应结存数量小于0！\n未执行删除！', QMessageBox.Yes)
                else:
                    QMessageBox.question(self, '删除出错！', '成功删除' + str(i) + '条入库记录！\n' + '下一条入库记录若删除，对应结存数量小于0，停止删除！',
                                         QMessageBox.Yes)
                cur.close()
                conn.close()
                (flag, res) = self.my_query()
                self.fill_table(res)
                return
            sql = "update material set now_num=" + str(new_num) + " where material_id='" + material_id_ll[i] + "'"
            cur.execute(sql)
            sql = "delete from in_log where in_log_id=" + id_ll[i]
            cur.execute(sql)
            conn.commit()
        cur.close()
        conn.close()
        QMessageBox.question(self, '删除成功！', str(len(indexs)) + '条入库记录已删除', QMessageBox.Yes)
        (flag, res) = self.my_query()
        self.fill_table(res)
        self.selected_row = -1

    def on_update_btn_clicked(self):
        indexs = self.tableView.selectionModel().selectedIndexes()
        tt = set()
        for t in indexs:
            tt.add(t.row())
        indexs = []
        for t in tt:
            indexs.append(t)
        if indexs == []:
            QMessageBox.question(self, '修改失败！', '请正确选择入库记录！', QMessageBox.Yes)
            return
        if len(indexs) > 1:
            QMessageBox.question(self, '修改失败！', '只能选中一行记录进行修改！', QMessageBox.Yes)
            return
        row_num = indexs[0]
        tlog_id = str(self.export_data[row_num][10])
        var.tin_log_id = tlog_id
        window = update_in_log_window()
        window.my_Signal.connect(self.refresh_after_update)
        window.show()
        self.selected_row = -1

    def refresh_after_update(self):
        (flag, res) = self.my_query()
        self.fill_table(res)

    def on_cancel_btn_clicked(self):
        self.close()

    def on_clear_query_btn_clicked(self):
        self.st_dateEdit.setDate(QDate(2000, 1, 1))
        self.ed_dateEdit.setDate(QDate(2050, 12, 31))
        self.spec_lineEdit.setText("")
        self.selected_row = -1
        self.id.setText("")
        self.name.setText("")
        self.user_lineEdit.setText("")
        self.agree_lineEdit.setText("")
        self.st_num.setText("")
        self.ed_num.setText("")
        (flag, res) = self.my_query()
        self.fill_table(res)

    def keyPressEvent(self, event):
        if str(event.key()) == '16777220' or str(event.key()) == '16777221':
            self.on_query_btn_clicked()
