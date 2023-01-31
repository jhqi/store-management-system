import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
import resources_rc
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QHeaderView
from lots_new import Ui_lots_new
import sqlite3


class lots_new_window(QMainWindow, Ui_lots_new):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.main_window = self
        self.setWindowIcon(QIcon(":/images/image.ico"))
        self.generate_pushButton.clicked.connect(self.on_generate_btn_clicked)
        self.clear_lists_pushButton.clicked.connect(self.on_clear_btn_clicked)
        self.cancel_pushButton.clicked.connect(self.on_cancel_btn_clicked)
        self.confirm_pushButton.clicked.connect(self.on_confirm_btn_clicked)
        self.fill_table([])
        self.generate_pushButton.setStyleSheet("background:#BFCAE6")
        self.confirm_pushButton.setStyleSheet("background:#BFCAE6")

    def on_cancel_btn_clicked(self):
        self.close()

    def on_confirm_btn_clicked(self):
        if self.export_data == []:
            QMessageBox.question(self, '操作失败！', '批量新增存货详单中没有数据！', QMessageBox.Yes)
            return
        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        sql = "insert into material values "
        for i in range(len(self.export_data)):
            # [id_ll[i], name_ll[i], spec_ll[i], unit_ll[i], ori_num_ll[i], price_ll[i], pos_ll[i]]
            sql+=f"('{self.export_data[i][0]}','{self.export_data[i][1]}','{self.export_data[i][2]}','{self.export_data[i][3]}','{str(self.export_data[i][5])}','{self.export_data[i][6]}','{str(self.export_data[i][4])}','{str(self.export_data[i][4])}')"
            if i < len(self.export_data)-1:
                sql+=','
            else:
                sql += ';'
        cur.execute(sql)
        conn.commit()
        QMessageBox.question(self, '批量新增存货成功！' , '批量操作完成！', QMessageBox.Yes)
        self.on_clear_btn_clicked()
        cur.close()
        conn.close()

    def fill_table(self, datas):  # datas为列表
        #[id_ll[i],name_ll[i],spec_ll[i],unit_ll[i],ori_num_ll[i],price_ll[i],pos_ll[i]]
        self.export_data = datas
        self.model = QStandardItemModel(len(datas), 7)
        self.model.setHorizontalHeaderLabels(
            ['存货编码', '存货名称', '规格型号', '计量单位', '单价(元)','库存位置','期初数量'])
        if datas != []:
            for i in range(0, len(datas)):
                item = QStandardItem(datas[i][0]) #id
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 0, item)

                item = QStandardItem(datas[i][1]) #name
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 1, item)

                item = QStandardItem(datas[i][2]) #spec
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 2, item)

                item = QStandardItem(datas[i][3]) #unit
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 3, item)

                item = QStandardItem(format(float(datas[i][5]), '.2f')) # 单价
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 4, item)

                item = QStandardItem(datas[i][6]) # 库存位置
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 5, item)

                item = QStandardItem(format(float(datas[i][4]), '.2f')) # 期初数量
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 6, item)

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
        self.tableView.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)

    def on_clear_btn_clicked(self):
        self.id_textEdit.setPlainText("")
        self.name_textEdit.setPlainText("")
        self.spec_textEdit.setPlainText("")
        self.unit_textEdit.setPlainText("")
        self.ori_num_textEdit.setPlainText("")
        self.pos_textEdit.setPlainText("")
        self.price_textEdit.setPlainText("")
        self.fill_table([])

    def on_generate_btn_clicked(self):
        id_str = self.id_textEdit.toPlainText()
        id_str = id_str.strip('\n\t ')
        if id_str == "":
            QMessageBox.question(self, '生成失败！', '存货编码不可为空！', QMessageBox.Yes)
            return

        id_ll = id_str.split('\n')
        id_len = len(id_ll)
        for i in range(0, id_len):
            id_ll[i] = id_ll[i].strip('\n\t ')
            if id_ll[i]=='':
                QMessageBox.question(self, '生成失败！', f'第{i+1}条存货编码为空！', QMessageBox.Yes)
                return

        # 判断重复
        for i in range(0, id_len):
            for j in range(i + 1, id_len):
                if id_ll[i] == id_ll[j]:
                    QMessageBox.question(self, '生成失败！', '存货编码列表第' + str(i + 1) + "行与第" + str(j + 1) + "行重复！\n请自行合并！",
                                         QMessageBox.Yes)
                    return

        name_str = self.name_textEdit.toPlainText()
        if name_str == "":
            QMessageBox.question(self, '生成失败！', '操作数量不可为空！', QMessageBox.Yes)
            return
        else:
            name_str = name_str.strip('\n\t ')
            name_ll = name_str.split('\n')

            if len(name_ll) != id_len:
                QMessageBox.question(self, '生成失败！', '存货名称列表条数与存货编码列表不一致！', QMessageBox.Yes)
                return
            for i in range(0, id_len):
                name_ll[i] = name_ll[i].strip('\n\t ')
                if name_ll[i] == '':
                    QMessageBox.question(self, '生成失败！', f'第{i + 1}条存货名称为空！', QMessageBox.Yes)
                    return

        spec_str = self.spec_textEdit.toPlainText()
        if spec_str == "":
            QMessageBox.question(self, '生成失败！', '规格型号不可为空！', QMessageBox.Yes)
            return
        else:
            spec_str = spec_str.strip('\n\t ')
            spec_ll = spec_str.split('\n')

            if len(spec_ll) != id_len:
                QMessageBox.question(self, '生成失败！', '规格型号列表条数与存货编码列表不一致！', QMessageBox.Yes)
                return
            for i in range(0, id_len):
                spec_ll[i] = spec_ll[i].strip('\n\t ')
                if spec_ll[i] == '':
                    QMessageBox.question(self, '生成失败！', f'第{i + 1}条规格型号为空！', QMessageBox.Yes)
                    return

        unit_str = self.unit_textEdit.toPlainText()
        if unit_str == "":
            QMessageBox.question(self, '生成失败！', '计量单位不可为空！', QMessageBox.Yes)
            return
        else:
            unit_str = unit_str.strip('\n\t ')
            unit_ll = unit_str.split('\n')

            if len(unit_ll) != id_len:
                QMessageBox.question(self, '生成失败！', '计量单位列表条数与存货编码列表不一致！', QMessageBox.Yes)
                return
            for i in range(0, id_len):
                unit_ll[i] = unit_ll[i].strip('\n\t ')
                if unit_ll[i] == '':
                    QMessageBox.question(self, '生成失败！', f'第{i + 1}条计量单位为空！', QMessageBox.Yes)
                    return

        ori_num_str = self.ori_num_textEdit.toPlainText()
        if ori_num_str == "":
            QMessageBox.question(self, '生成失败！', '期初数量不可为空！', QMessageBox.Yes)
            return
        else:
            ori_num_str = ori_num_str.strip('\n\t ')
            ori_num_ll = ori_num_str.split('\n')

            if len(ori_num_ll) != id_len:
                QMessageBox.question(self, '生成失败！', '期初数量列表条数与存货编码列表不一致！', QMessageBox.Yes)
                return
            for i in range(0, id_len):
                ori_num_ll[i] = ori_num_ll[i].strip('\n\t ')
                try:
                    ori_num_ll[i]=float(ori_num_ll[i])
                except:
                    QMessageBox.question(self, '生成失败！', '第' + str(i + 1) + "条期初数量不是实数！",QMessageBox.Yes)
                    return

        pos_str = self.pos_textEdit.toPlainText()
        if pos_str == "":
            QMessageBox.question(self, '生成失败！', '库存位置不可为空！', QMessageBox.Yes)
            return
        else:
            pos_str = pos_str.strip('\n\t ')
            pos_ll = pos_str.split('\n')

            if len(pos_ll) != id_len:
                QMessageBox.question(self, '生成失败！', '库存位置列表条数与存货编码列表不一致！', QMessageBox.Yes)
                return
            for i in range(0, id_len):
                pos_ll[i] = pos_ll[i].strip('\n\t ')
                if pos_ll[i] == '':
                    QMessageBox.question(self, '生成失败！', f'第{i + 1}条库存位置为空！', QMessageBox.Yes)
                    return

        price_str = self.price_textEdit.toPlainText()
        if price_str == "":
            QMessageBox.question(self, '生成失败！', '单价不可为空！', QMessageBox.Yes)
            return
        else:
            price_str = price_str.strip('\n\t ')
            price_ll = price_str.split('\n')

            if len(price_ll) != id_len:
                QMessageBox.question(self, '生成失败！', '单价列表条数与存货编码列表不一致！', QMessageBox.Yes)
                return
            for i in range(0, id_len):
                price_ll[i] = price_ll[i].strip('\n\t ')
                try:
                    price_ll[i]=float(price_ll[i])
                except:
                    QMessageBox.question(self, '生成失败！', '第' + str(i + 1) + "条单价不是实数！",QMessageBox.Yes)
                    return

        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        sql = "select material_id from material"
        cur.execute(sql)
        exist_id=cur.fetchall()
        for i in range(len(exist_id)):
            exist_id[i]=exist_id[i][0]

        #判断有无重复物料编码
        for i in range(len(id_ll)):
            if id_ll[i] in exist_id:
                QMessageBox.question(self, '生成失败！', '第' + str(i + 1) + "条存货编码重复，已在库中！", QMessageBox.Yes)
                cur.close()
                conn.close()
                return

        table_data = []
        for i in range(len(id_ll)):
            tmp=[id_ll[i],name_ll[i],spec_ll[i],unit_ll[i],ori_num_ll[i],price_ll[i],pos_ll[i]]
            table_data.append(tmp)

        self.fill_table(table_data)
        QMessageBox.question(self, '生成成功！', "批量新增存货详单已填充至下方表格，请仔细核查！", QMessageBox.Yes)
