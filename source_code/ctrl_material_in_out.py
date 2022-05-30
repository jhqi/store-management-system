import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
import resources_rc
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from material_in_out import Ui_material_in_out
from objects import In_Log, Out_Log
import sqlite3


class material_in_log_window(QMainWindow, Ui_material_in_out):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.main_window = self
        self.setWindowIcon(QIcon(":/images/image.ico"))
        self.dateEdit.setDate(QDate.currentDate())
        self.selected_row = -1
        self.tableView.clicked.connect(self.on_tableview_select_item)
        self.init_table()
        self.confirm_pushButton.clicked.connect(self.on_confirm_btn_clicked)
        self.cancel_pushButton.clicked.connect(self.on_cancel_btn_clicked)
        self.list_all_pushButton.clicked.connect(self.on_list_all_btn_clicked)
        self.unit_lineEdit.setReadOnly(True)
        self.per_price_lineEdit.setReadOnly(True)
        self.position_lineEdit.setReadOnly(True)
        self.now_num_lineEdit.setReadOnly(True)
        self.label_5.setStyleSheet('color:red')
        self.comboBox.currentIndexChanged.connect(lambda: self.on_combobox_changed(self.comboBox.currentIndex()))

    def on_combobox_changed(self, idx):
        if idx == 0:
            self.confirm_label.setText("")
        elif idx == 1:
            self.confirm_label.setText("入库操作")
            self.confirm_label.setStyleSheet("color:red")
        else:
            self.confirm_label.setText("出库操作")
            self.confirm_label.setStyleSheet("color:green")

    def fill_table(self, datas):  # datas为列表
        self.export_data = datas
        self.model = QStandardItemModel(len(datas), 5)
        self.model.setHorizontalHeaderLabels(['存货编码', '存货名称', '规格型号', '库存位置', '结存数量'])
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

                item = QStandardItem(format(float(str(datas[i][4])), '.4f'))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 4, item)

        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()
        self.tableView.resizeRowsToContents()
        self.tableView.horizontalHeader().setStretchLastSection(True)

    def on_tableview_select_item(self, event):
        self.selected_row = self.tableView.currentIndex().row()
        try:
            tid = self.model.item(self.selected_row, 0).text()
        except:
            QMessageBox.question(self, '选择失败！', '请选择表中一条记录！', QMessageBox.Yes)
        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        sql = "select material_id,material_name,spec,unit,per_price,pos,now_num from material where material_id='" + tid + "'"
        cur.execute(sql)
        res = cur.fetchone()
        cur.close()
        conn.close()
        self.material_id_lineEdit.setText(res[0])
        self.material_name_lineEdit.setText(res[1])
        self.spec_lineEdit.setText(res[2])
        self.unit_lineEdit.setText(res[3])
        if res[4] == -1:
            self.per_price_lineEdit.setText('未知')
        else:
            self.per_price_lineEdit.setText(str(res[4]))
        self.position_lineEdit.setText(res[5])
        self.now_num_lineEdit.setText(str(res[6]))

    def init_table(self):
        sql = "select material_id,material_name,spec,pos, now_num from material"
        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        cur.execute(sql)
        datas = cur.fetchall()
        self.export_data = datas
        cur.close()
        conn.close()
        self.model = QStandardItemModel(len(datas), 5)
        self.model.setHorizontalHeaderLabels(['存货编码', '存货名称', '规格型号', '库存位置', '结存数量'])
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

                item = QStandardItem(format(float(str(datas[i][4])), '.4f'))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 4, item)

        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()
        self.tableView.resizeRowsToContents()
        self.tableView.horizontalHeader().setStretchLastSection(True)

    def on_confirm_btn_clicked(self):
        name = self.material_name_lineEdit.text()
        name = name.strip("\n \t")
        id = self.material_id_lineEdit.text()
        id = id.strip("\n \t")
        spec = self.spec_lineEdit.text()
        spec = spec.strip("\n \t")
        log_date = self.dateEdit.date().toString(Qt.ISODate)
        ll = log_date.split('-')
        log_date = "".join(ll)
        num = self.change_num_lineEdit.text()
        user_man = self.user_man_lineEdit.text()
        user_man = user_man.strip("\n \t")
        if user_man == "":
            user_man = "未知"
        agree_man = self.agree_man_lineEdit.text()
        agree_man = agree_man.strip("\n \t")
        if agree_man == "":
            QMessageBox.question(self, '操作失败！', '令号不可为空！', QMessageBox.Yes)
            return
        try:
            num_value = float(num)
        except:
            QMessageBox.question(self, '操作失败！', '操作数量必须是实数！', QMessageBox.Yes)
            return

        before_num = float(self.now_num_lineEdit.text())
        if self.comboBox.currentIndex() == 0:
            QMessageBox.question(self, '操作失败！', '请选择操作类型！', QMessageBox.Yes)
            return
        elif self.comboBox.currentIndex() == 1:
            log_type = "入库"
        else:
            log_type = "出库"

        if log_type == "出库" and before_num < num_value:
            QMessageBox.question(self, '出库失败！', '库存不足！', QMessageBox.Yes)
            return

        per_price = self.per_price_lineEdit.text()
        position = self.position_lineEdit.text()
        if per_price == '未知':
            total_price = '-1'
            per_price = '-1'
        else:
            total_price = str(float(per_price) * float(num))

        if log_type == "入库":
            after_num = before_num + num_value
            after_num = str(after_num)
            tmp_in_log = In_Log(log_date, id, name, spec, num, per_price, position, total_price, user_man, agree_man)
            tmp_in_log.new_in_log()
        else:
            after_num = before_num - num_value
            after_num = str(after_num)
            tmp_out_log = Out_Log(log_date, id, name, spec, num, per_price, position, total_price, user_man, agree_man)
            tmp_out_log.new_out_log()

        # 更新材料表中的结存数量
        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        sql = "update material set now_num=" + after_num + " where material_id='" + id + "'"
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

        # 清空、重新加载数据
        self.init_table()
        self.material_name_lineEdit.setText("")
        self.material_id_lineEdit.setText("")
        self.spec_lineEdit.setText("")
        self.unit_lineEdit.setText("")
        self.now_num_lineEdit.setText("")
        self.comboBox.setCurrentIndex(0)
        self.dateEdit.setDate(QDate.currentDate())
        self.change_num_lineEdit.setText("")
        self.user_man_lineEdit.setText("")
        self.agree_man_lineEdit.setText("")
        self.per_price_lineEdit.setText("")
        self.position_lineEdit.setText("")

        if log_type == "入库":
            QMessageBox.question(self, '入库成功！', '存货成功入库！', QMessageBox.Yes)
        else:
            QMessageBox.question(self, '出库成功！', '存货成功出库！', QMessageBox.Yes)

    def on_cancel_btn_clicked(self):
        self.close()

    def on_list_all_btn_clicked(self):
        self.init_table()

    def keyPressEvent(self, event):
        if str(event.key()) == '16777220' or str(event.key()) == '16777221':
            if self.material_name_lineEdit.text() == "" and self.material_id_lineEdit.text() == "" and self.spec_lineEdit.text() == "":
                QMessageBox.question(self, '查询失败！', '请输入存货编码或存货名称或规格型号！', QMessageBox.Yes)
                self.fill_table([])
                return
            conn = sqlite3.connect("material_management.db")
            conn.text_factory = str
            cur = conn.cursor()
            sql = "select material_id,material_name,spec,pos, now_num from material "
            has_where = False
            if self.material_id_lineEdit.text() != "":
                if has_where == True:
                    sql += " and material_id='" + self.material_id_lineEdit.text() + "'"
                else:
                    sql += "where material_id='" + self.material_id_lineEdit.text() + "'"
                    has_where = True
            if self.material_name_lineEdit != "":
                name = self.material_name_lineEdit.text()
                name1 = "%%" + name + "%%"
                name2 = "%" + name + "%"
                if has_where == True:
                    sql += " and (material_name like '" + name1 + "' or material_name like '" + name2 + "') "
                else:
                    sql += "where (material_name like '" + name1 + "' or material_name like '" + name2 + "') "
                    has_where = True
            if self.spec_lineEdit.text() != "":
                name = self.spec_lineEdit.text()
                name1 = "%%" + name + "%%"
                name2 = "%" + name + "%"
                if has_where == True:
                    sql += " and (spec like '" + name1 + "' or spec like '" + name2 + "') "
                else:
                    sql += "where (spec like '" + name1 + "' or spec like '" + name2 + "') "
                    has_where
            cur.execute(sql)
            res = cur.fetchall()
            cur.close()
            conn.close()
            if res == []:
                QMessageBox.question(self, '查询失败！', '未找到相关存货！', QMessageBox.Yes)
                self.fill_table([])
                return
            self.fill_table(res)
            # 清空、重新加载数据
            # self.init_table()
            self.material_name_lineEdit.setText("")
            self.material_id_lineEdit.setText("")
            self.spec_lineEdit.setText("")
            self.unit_lineEdit.setText("")
            self.now_num_lineEdit.setText("")
            self.comboBox.setCurrentIndex(0)
            self.dateEdit.setDate(QDate.currentDate())
            self.change_num_lineEdit.setText("")
            self.user_man_lineEdit.setText("")
            self.agree_man_lineEdit.setText("")
            self.per_price_lineEdit.setText("")
            self.position_lineEdit.setText("")
            QMessageBox.question(self, '查询成功！', '相关结果列在右侧表格中，\n请具体选择！', QMessageBox.Yes)
