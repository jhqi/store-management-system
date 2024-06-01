import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
import resources_rc
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QMessageBox, QInputDialog
from shoufacun_info import Ui_shoufacun_info
import sqlite3
import datetime
from openpyxl import Workbook
import time
import copy


class shoufacun_info_window(QMainWindow, Ui_shoufacun_info):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.main_window = self
        self.setWindowIcon(QIcon(":/images/image.ico"))
        self.query_btn.setStyleSheet("background:#FF95CA")
        self.st_dateEdit.setDate(QDate(2000, 1, 1))

        #截止日期默认设置为当天
        d=datetime.datetime.now()
        self.ed_dateEdit.setDate(QDate(d.year, d.month, d.day))

        #连接数据库，默认列出所有存货的累计收入、发出、截止日期日操作完成后的结存
        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        sql = "select material_id, sum(in_num) from in_log group by material_id"
        cur.execute(sql)
        in_res = cur.fetchall()

        sql = "select material_id, sum(out_num) from out_log group by material_id"
        cur.execute(sql)
        out_res = cur.fetchall()

        sql = "select material_id, material_name, spec, ori_num from material"
        cur.execute(sql)
        ori_num_res = cur.fetchall()

        in_dic={}
        for tmp in in_res:
            in_dic[tmp[0]]=tmp[1]

        out_dic={}
        for tmp in out_res:
            out_dic[tmp[0]]=tmp[1]

        #不设置任何筛选条件的所有结果
        self.initial_res=[]
        for tmp in ori_num_res:
            material_id=tmp[0]
            material_name=tmp[1]
            spec=tmp[2]
            ori_num=tmp[3]
            in_num=0
            out_num=0
            if material_id in in_dic.keys():
                in_num=in_dic[material_id]
            if material_id in out_dic.keys():
                out_num = out_dic[material_id]
            now_num=ori_num+in_num-out_num
            self.initial_res.append(
                (material_id, material_name, spec, ori_num, in_num, out_num, now_num)
            )
        cur.close()
        conn.close()
        self.export_data=[]
        self.fill_table(self.initial_res)
        self.cancel_btn.clicked.disconnect()
        self.query_btn.clicked.disconnect()

        self.cancel_btn.clicked.connect(self.on_cancel_btn_clicked)
        self.query_btn.clicked.connect(self.on_query_btn_clicked)
        self.export_excel.clicked.connect(self.on_export_btn_clicked)

    def fill_table(self, datas):  # datas为列表
        self.export_data = datas
        self.model = QStandardItemModel(len(datas), 7)
        self.model.setHorizontalHeaderLabels(
            ['存货编码', '存货名称', '规格型号', '期初数量', '总收入数量', '总发出数量', '结存数量'])
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

                item = QStandardItem(format(datas[i][3], '.2f'))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 3, item)

                item = QStandardItem(format(datas[i][4], '.2f'))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 4, item)

                item = QStandardItem(format(datas[i][5], '.2f'))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.model.setItem(i, 5, item)

                item = QStandardItem(format(datas[i][6], '.2f'))
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
        # self.tableView.horizontalHeader().setSectionsClickable(True)
        # self.tableView.setSortingEnabled(False)
        # self.tableView.setSortingEnabled(True)

    @staticmethod
    def sql_res2dict(res, tmp_dic):
        if res!=[]:
            for tmp in res:
                tmp_dic[tmp[0]]=tmp[1]
        return tmp_dic

    def my_query(self):
        st_date = self.st_dateEdit.date().toString(Qt.ISODate)
        ll = st_date.split('-')
        st_date = "".join(ll)
        ed_date = self.ed_dateEdit.date().toString(Qt.ISODate)
        ll = ed_date.split('-')
        ed_date = "".join(ll)
        d = datetime.datetime.now()
        today_date=f'{d.year}{str(d.month).zfill(2)}{str(d.day).zfill(2)}'
        if ed_date>today_date: #截止日期不可大于当天
            return (0, [])

        if st_date > ed_date: #起始日期大于截止日期
            return (1, [])

        id_ll=None
        name_ll=None
        spec_ll=None

        if self.id.text() != "":
            id_str = self.id.text()
            id_str = id_str.strip(';\n\t ')
            id_ll = id_str.split(';')

        if self.name.text() != "":
            name_str = self.name.text()
            name_str = name_str.strip(';\n\t ')
            name_ll = name_str.split(';')
            name_ll1 = []
            name_ll2 = []
            for tname in name_ll:
                name_ll1.append("%" + tname + "%")
                name_ll2.append("%%" + tname + "%%")

        if self.spec_lineEdit.text() != "":
            spec_str = self.spec_lineEdit.text()
            spec_str = spec_str.strip(';\n\t ')
            spec_ll = spec_str.split(';')
            spec_ll1 = []
            spec_ll2 = []
            for tspec in spec_ll:
                spec_ll1.append("%" + tspec + "%")
                spec_ll2.append("%%" + tspec + "%%")

        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        sql='select material_id, material_name, spec from material'

        have_where=False

        if id_ll is not None:
            sql+=' where ('
            have_where=True
            for i in range(len(id_ll)):
                sql += f"material_id like \'%{id_ll[i]}%\'"
                if i < len(id_ll) - 1:
                    sql += " or "
            sql += ")"

        if name_ll is not None:
            if have_where:
                sql += " and ("
            else:
                sql+=' where ('
                have_where=True
            for i in range(len(name_ll)):
                sql += "material_name like '" + name_ll1[i] + "' or material_name like '" + name_ll2[i] + "'"
                if i < len(name_ll) - 1:
                    sql += " or "
            sql += ")"

        if spec_ll is not None:
            if have_where:
                sql += " and ("
            else:
                sql+=' where ('
                have_where=True
            for i in range(len(spec_ll)):
                sql += "spec like '" + spec_ll1[i] + "' or spec like '" + spec_ll2[i] + "'"
                if i < len(spec_ll) - 1:
                    sql += " or "
            sql += ")"

        cur.execute(sql)
        id_name_spec = cur.fetchall()
        # cur.close()
        # conn.close()
        if id_name_spec == []: #不存在相关存货记录
            return (2, [])

        selected_id=[]
        for tmp in id_name_spec:
            selected_id.append(tmp[0])

        #辅助变量，不用重复生成初始字典
        tmp_dic={}
        for id in selected_id:
            tmp_dic[id]=0

        id_name_dic={}
        id_spec_dic={}
        for tmp in id_name_spec:
            id_name_dic[tmp[0]]=tmp[1]
            id_spec_dic[tmp[0]]=tmp[2]

        #查询这些存货在开始日期前的结存数量，即表格中显示的期初数量
        #分别查这些存货在开始日期前的总收入、总发出

        #sql拼接or不得超过1000条，考虑换成关键字in，并且优化针对全体物料的查询
        selected_id_str=""
        null_flag=False
        if (id_ll is None) and (name_ll is None) and (spec_ll is None): #全体物料
            null_flag=True
            in_sql=f"select material_id, sum(in_num) from in_log where date_time < '{st_date}' group by material_id"
            out_sql=f"select material_id, sum(out_num) from out_log where date_time < '{st_date}' group by material_id"
        else:
            #生成selected_id用于in查询的字符串
            for id in selected_id:
                selected_id_str+="\'"+id+"\'"+','
            selected_id_str=selected_id_str[:-1]
            in_sql=f"select material_id, sum(in_num) from in_log where material_id in({selected_id_str}) and date_time < '{st_date}' group by material_id"
            out_sql=f"select material_id, sum(out_num) from out_log where material_id in({selected_id_str}) and date_time < '{st_date}' group by material_id"

        cur.execute(in_sql)
        id_in_before=cur.fetchall()
        tt_dic=copy.deepcopy(tmp_dic)
        id_in_before=self.sql_res2dict(id_in_before, tt_dic)

        cur.execute(out_sql)
        id_out_before = cur.fetchall()
        tt_dic=copy.deepcopy(tmp_dic)
        id_out_before = self.sql_res2dict(id_out_before, tt_dic)

        #再查这些存货的期初数量
        if null_flag:
            sql = 'select material_id, ori_num from material'
        else:
            sql = f'select material_id, ori_num from material where material_id in ({selected_id_str})'
        
        cur.execute(sql)
        id_ori_num = cur.fetchall()
        tt_dic=copy.deepcopy(tmp_dic)
        id_ori_num = self.sql_res2dict(id_ori_num, tt_dic)

        #算出来开始日期前的结存，即表格中的期初
        table_ori_num={}
        for tid in selected_id:
            table_ori_num[tid]=id_ori_num[tid]+id_in_before[tid]-id_out_before[tid]

        #再查时间段内的总收入，总发出
        if null_flag:
            in_sql=f"select material_id, sum(in_num) from in_log where date_time >= '{st_date}' and date_time <= '{ed_date}' group by material_id"
            out_sql=f"select material_id, sum(out_num) from out_log where date_time >= '{st_date}' and date_time <= '{ed_date}' group by material_id"
        else:
            in_sql=f"select material_id, sum(in_num) from in_log where material_id in({selected_id_str}) and date_time >= '{st_date}' and date_time <= '{ed_date}' group by material_id"
            out_sql=f"select material_id, sum(out_num) from out_log where material_id in({selected_id_str}) and date_time >= '{st_date}' and date_time <= '{ed_date}' group by material_id"

        cur.execute(in_sql)
        id_period_in_num = cur.fetchall()
        tt_dic=copy.deepcopy(tmp_dic)
        id_period_in_num = self.sql_res2dict(id_period_in_num, tt_dic)

        cur.execute(out_sql)
        id_period_out_num = cur.fetchall()
        tt_dic=copy.deepcopy(tmp_dic)
        id_period_out_num = self.sql_res2dict(id_period_out_num, tt_dic)

        #最后整合
        query_res=[]
        for tid in selected_id:
            tmp=(
                tid, id_name_dic[tid], id_spec_dic[tid], table_ori_num[tid], id_period_in_num[tid], id_period_out_num[tid], table_ori_num[tid]+id_period_in_num[tid]-id_period_out_num[tid]
            )
            query_res.append(tmp)

        return (3, query_res)

    def on_query_btn_clicked(self):
        (flag, res) = self.my_query()
        if flag == 0:
            QMessageBox.question(self, '查询失败！', '截止日期不应超出当天！', QMessageBox.Yes)
            self.fill_table([])
            d = datetime.datetime.now()
            self.ed_dateEdit.setDate(QDate(d.year, d.month, d.day))
            return
        elif flag == 1:
            QMessageBox.question(self, '查询失败！', '开始日期不应大于截止日期！', QMessageBox.Yes)
            self.fill_table([])
            return
        elif flag == 2:
            QMessageBox.question(self, '查询失败！', '未查询到相关存货！', QMessageBox.Yes)
            self.fill_table([])
            return
        else:
            self.fill_table(res)
            QMessageBox.question(self, '查询成功！', '相关收发存数据已列在表中！', QMessageBox.Yes)

    def on_clear_query_btn_clicked(self):
        self.st_dateEdit.setDate(QDate(2000, 1, 1))
        d = datetime.datetime.now()
        self.ed_dateEdit.setDate(QDate(d.year, d.month, d.day))
        self.spec_lineEdit.setText("")
        self.id.setText("")
        self.name.setText("")
        self.fill_table(self.initial_res)

    def on_export_btn_clicked(self):
        if self.export_data == []:
            QMessageBox.question(self, '导出失败！', '请确认表中存在收发存数据！', QMessageBox.Yes)
            return
        book = Workbook()
        sheet = book.active
        sheet.append(('开始日期(含)', '截至日期(含)', '存货编码', '存货名称', '规格型号', '期初数量', '总收入数量', '总发出数量', '结存数量'))

        #获取开始日期、截至日期
        st_date_qt = self.st_dateEdit.date()
        st_date=datetime.date(st_date_qt.year(), st_date_qt.month(), st_date_qt.day())
        ed_date_qt=self.ed_dateEdit.date()
        ed_date = datetime.date(ed_date_qt.year(), ed_date_qt.month(), ed_date_qt.day())
        for i in range(len(self.export_data)):
            tmp = (st_date, ed_date, self.export_data[i][0], self.export_data[i][1], self.export_data[i][2], self.export_data[i][3],
                   self.export_data[i][4], self.export_data[i][5], self.export_data[i][6])
            sheet.append(tmp)

        tmp_dialog = QtWidgets.QFileDialog(None, "选取收发存数据保存路径", "C:/")
        tmp_dialog.setLabelText(QtWidgets.QFileDialog.Accept, '确认')
        tmp_dialog.setLabelText(QtWidgets.QFileDialog.Reject, '取消')
        tmp_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        if tmp_dialog.exec_():
            ll = tmp_dialog.selectedFiles()
            dir_path = ll[0]
        else:
            return
        time_str = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        file_name = time_str + "收发存数据.xlsx"
        content, conform = QInputDialog.getText(self.main_window, '文件名', '请输入文件名：', text=file_name)
        if conform:
            file_name = content
        else:
            return
        try:
            book.save(dir_path + "/" + file_name)
            QMessageBox.question(self, '导出成功！', '收发存数据已导出至Excel！', QMessageBox.Yes)
        except:
            QMessageBox.question(self, '导出失败！', '文件名有误！', QMessageBox.Yes)

    def on_cancel_btn_clicked(self):
        self.close()

    def keyPressEvent(self, event):
        if str(event.key()) == '16777220' or str(event.key()) == '16777221':
            self.on_query_btn_clicked()