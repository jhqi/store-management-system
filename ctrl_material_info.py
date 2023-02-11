import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
import resources_rc
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QInputDialog, QHeaderView
from PyQt5 import QtWidgets
from material_info import Ui_material_info
from ctrl_update_material import update_material_window
from ctrl_total_data import total_data_window
from ctrl_del_confirm import del_confirm_window
import sqlite3
from openpyxl import Workbook
import time


class material_info_window(QMainWindow, Ui_material_info):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.main_window = self
        self.setWindowIcon(QIcon(":/images/image.ico"))
        self.query_btn.setStyleSheet("background:#FF95CA")
        self.selected_row = -1
        self.selected_row_ll = []
        self.del_material_btn.clicked.disconnect()
        self.query_btn.clicked.disconnect()
        self.update_btn.clicked.disconnect()
        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        cur.execute("select * from material")
        res = cur.fetchall()
        cur.close()
        conn.close()
        self.fill_table(res)

        # self.query_btn.clicked.disconnect()
        self.total_data_btn.clicked.disconnect()

        self.del_material_btn.clicked.connect(self.on_del_material_btn_clicked)
        # self.del_both_btn.clicked.connect(self.on_del_both_btn_clicked)
        self.update_btn.clicked.connect(self.on_update_btn_clicked)
        self.cancel.clicked.connect(self.on_cancel_btn_clicked)
        self.query_btn.clicked.connect(self.on_query_btn_clicked)
        self.clear_query_info.clicked.connect(self.on_clear_query_btn_clicked)
        self.tableView.clicked.connect(self.on_tableview_select_item)
        self.export_excel.clicked.connect(self.on_export_btn_clicked)
        self.total_data_btn.clicked.connect(self.on_total_data_btn_clicked)

        # self.query_btn_lock=False
        # self.query_btn.installEventFilter(self)

    # def eventFilter(self, object, event):
    #     if event.type() == QtCore.QEvent.HoverMove:
    #         self.query_btn_lock = False
    #         return True
    #     return False
    def on_total_data_btn_clicked(self):
        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        sql="select count(*) from material"
        cur.execute(sql)
        res=cur.fetchone()
        if res[0]==0:
            QMessageBox.question(self, '汇总统计失败！', '存货表为空！', QMessageBox.Yes)
            return

        window = total_data_window()
        window.show()


    def on_export_btn_clicked(self):
        if self.export_data == []:
            QMessageBox.question(self, '导出失败！', '请确认表中存在物料数据！', QMessageBox.Yes)
            return
        book = Workbook()
        book.iso_dates = True
        sheet = book.active
        sheet.append(('存货编码', '存货名称', '规格型号', '计量单位', '单价(元)', '库存位置', '期初数量', '结存数量'))
        for row in self.export_data:
            sheet.append(row)

        tmp_dialog = QtWidgets.QFileDialog(None, "选取存货数据保存路径", "C:/")
        tmp_dialog.setLabelText(QtWidgets.QFileDialog.Accept, '确认')
        tmp_dialog.setLabelText(QtWidgets.QFileDialog.Reject, '取消')
        tmp_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        if tmp_dialog.exec_():
            ll = tmp_dialog.selectedFiles()
            dir_path = ll[0]
        else:
            return
        time_str = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        file_name = time_str + "存货数据.xlsx"
        content, conform = QInputDialog.getText(self.main_window, '文件名', '请输入文件名：', text=file_name)
        if conform:
            file_name = content
        else:
            return
        try:
            book.save(dir_path + "/" + file_name)
            QMessageBox.question(self, '导出成功！', '存货数据已导出至Excel！', QMessageBox.Yes)
        except:
            QMessageBox.question(self, '导出失败！', '文件名有误！', QMessageBox.Yes)

    def fill_table(self, datas):  # datas为列表
        self.export_data = datas
        self.model = QStandardItemModel(len(datas), 8)
        self.model.setHorizontalHeaderLabels(['存货编码', '存货名称', '规格型号', '计量单位', '单价(元)', '库存位置', '期初数量', '结存数量'])
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

                tper_price = datas[i][4]
                if tper_price == -1:
                    tper_price = '未知'
                else:
                    tper_price = format(tper_price, '.2f')
                item = QStandardItem(tper_price)
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 4, item)

                item = QStandardItem(datas[i][5])
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 5, item)

                item = QStandardItem(format(datas[i][6], '.2f'))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 6, item)

                item = QStandardItem(format(datas[i][7], '.2f'))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 7, item)

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
        self.tableView.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)

    def my_query(self):
        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        flag1 = self.st_num.text() == ""
        flag2 = self.ed_num.text() == ""
        flag3 = self.st_per_price.text() == ""
        flag4 = self.ed_per_price.text() == ""

        # if self.st_num.text()=="" or self.ed_num=="" or self.st_per_price=="" or self.ed_per_price=="":
        #     QMessageBox.question(self, '查询失败！', "结存数量和单价范围不可为空！\n这两项不做筛选请点击\"清楚筛选\"恢复默认值！", QMessageBox.Yes)
        #     return
        if not flag1:
            try:
                st_num_value = float(self.st_num.text())
            except:
                return (-2, [])
        if not flag2:
            try:
                ed_num_value = float(self.ed_num.text())
            except:
                return (-2, [])
        if not flag3:
            try:
                st_per_price_value = float(self.st_per_price.text())
            except:
                return (-3, [])
        if not flag4:
            try:
                ed_per_price_value = float(self.ed_per_price.text())
            except:
                return (-3, [])

        if not flag1 and not flag2 and st_num_value > ed_num_value:
            return (-1, [])

        if not flag3 and not flag4 and st_per_price_value > ed_per_price_value:
            return (0, [])

        st_num = self.st_num.text()
        ed_num = self.ed_num.text()
        st_per_price = self.st_per_price.text()
        ed_per_price = self.ed_per_price.text()
        if flag1:
            st_num = "0"
        if flag2:
            ed_num = "999999999"
        if flag3:
            st_per_price = "0"
        if flag4:
            ed_per_price = "999999999"
        sql = "select * from material where (now_num between " + st_num + " and " + ed_num + " ) and (per_price between " + st_per_price + " and " + ed_per_price + " or per_price=-1) "
        if self.id.text() != "":
            id_ll = self.id.text()
            id_ll = id_ll.strip('%\n\t ')
            id_ll = id_ll.split('%')
            sql += " and ("
            for i in range(len(id_ll)):
                sql += "material_id='" + id_ll[i] + "'"
                if i < len(id_ll) - 1:
                    sql += " or "
            sql += ")"

        if self.name.text() != "":
            name_ll = self.name.text()
            name_ll = name_ll.strip('%\n\t ')
            name_ll = name_ll.split('%')
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
            spec_ll = self.spec_lineEdit.text()
            spec_ll = spec_ll.strip('%\n\t ')
            spec_ll = spec_ll.split('%')
            spec_ll1 = []
            spec_ll2 = []
            for tspec in spec_ll:
                spec_ll1.append("%" + tspec + "%")
                spec_ll2.append("%%" + tspec + "%%")
            sql += " and ("
            for i in range(len(spec_ll)):
                sql += "spec like '" + spec_ll1[i] + "' or spec like '" + spec_ll2[i] + "'"
                if i < len(spec_ll) - 1:
                    sql += " or "
            sql += ")"

        if self.position_lineEdit.text() != "":
            pos_ll = self.position_lineEdit.text()
            pos_ll = pos_ll.strip('%\n\t ')
            pos_ll = pos_ll.split('%')
            pos_ll1 = []
            pos_ll2 = []
            for tpos in pos_ll:
                pos_ll1.append("%" + tpos + "%")
                pos_ll2.append("%%" + tpos + "%%")
            sql += " and ("
            for i in range(len(pos_ll)):
                sql += "pos like '" + pos_ll1[i] + "' or pos like '" + pos_ll2[i] + "'"
                if i < len(pos_ll) - 1:
                    sql += " or "
            sql += ")"

        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        conn.close()
        if res == []:
            return (1, [])
        return (2, res)

    def on_query_btn_clicked(self):
        # if self.query_btn_lock:
        #     return
        # self.query_btn_lock=True
        (flag, res) = self.my_query()
        if flag == -1:
            QMessageBox.question(self, '查询失败！', "结存数量范围冲突！", QMessageBox.Yes)
            self.fill_table([])
        elif flag == 0:
            QMessageBox.question(self, '查询失败！', "单价范围冲突！", QMessageBox.Yes)
            self.fill_table([])
        elif flag == 1:
            QMessageBox.question(self, '查询失败！', '未查询到相关物料！', QMessageBox.Yes)
            self.fill_table([])
        elif flag == -2:
            QMessageBox.question(self, '查询失败！', '结存数量应输入实数！', QMessageBox.Yes)
            self.fill_table([])
        elif flag == -3:
            QMessageBox.question(self, '查询失败！', '单价应输入实数！', QMessageBox.Yes)
            self.fill_table([])
        else:
            self.fill_table(res)
            QMessageBox.question(self, '查询成功！', '查询结果位于表格中', QMessageBox.Yes)

    def on_tableview_select_item(self, event):
        self.selected_row = self.tableView.currentIndex().row()
        # self.tableView.selectRow(self.selected_row)

    def on_clear_query_btn_clicked(self):
        self.id.setText("")
        self.name.setText("")
        self.spec_lineEdit.setText("")
        self.position_lineEdit.setText("")
        self.st_num.setText("")
        self.ed_num.setText("")
        self.st_per_price.setText("")
        self.ed_per_price.setText("")
        (flag, res) = self.my_query()
        self.fill_table(res)

    def on_del_material_btn_clicked(self):
        indexs = self.tableView.selectionModel().selectedIndexes()
        tt = set()
        for t in indexs:
            tt.add(t.row())
        indexs = []
        for t in tt:
            indexs.append(t)
        if indexs == []:
            QMessageBox.question(self, '删除失败！', '请正确选择存货！', QMessageBox.Yes)
            return
        id_ll = []
        for index in indexs:
            row_num = index
            tid = self.model.item(row_num, 0).text()
            id_ll.append(tid)

        del_material_num=len(indexs)
        del_type=1 #删除存货，及存货对应的入库、出库信息

        window=del_confirm_window(del_type=del_type, del_num=del_material_num, del_ids=id_ll)
        window.del_finish_Signal.connect(self.refresh_after_update)
        window.show()

    def refresh_after_update(self):
        (flag, res) = self.my_query()
        self.fill_table(res)

    def on_update_btn_clicked(self):
        indexs = self.tableView.selectionModel().selectedIndexes()
        tt = set()
        for t in indexs:
            tt.add(t.row())
        indexs = []
        for t in tt:
            indexs.append(t)
        if indexs == []:
            QMessageBox.question(self, '修改失败！', '请正确选择物料！', QMessageBox.Yes)
            return
        if len(indexs) > 1:
            QMessageBox.question(self, '修改失败！', '只能选中一行记录进行修改！', QMessageBox.Yes)
            return
        row_num = indexs[0]
        tid = self.model.item(row_num, 0).text()
        window = update_material_window(tid=tid)
        window.my_Signal.connect(self.refresh_after_update)
        window.show()

    def on_cancel_btn_clicked(self):
        self.close()

    def keyPressEvent(self, event):
        if str(event.key()) == '16777220' or str(event.key()) == '16777221':
            self.on_query_btn_clicked()
