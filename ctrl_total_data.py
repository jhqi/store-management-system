import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
import resources_rc
from PyQt5.QtGui import  QIcon
from PyQt5.QtWidgets import QMainWindow
from total_data import Ui_total_data
import sqlite3


class total_data_window(QMainWindow, Ui_total_data):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.main_window = self
        self.setWindowIcon(QIcon(":/images/image.ico"))
        # self.cancel_pushButton.clicked.disconnect()
        self.cancel_pushButton.clicked.connect(self.on_cancel_btn_clicked)

        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        sql = "select material_id,ori_num,now_num from material"
        cur.execute(sql)
        res = cur.fetchall()
        all_material_map = {}
        total_ori_num=0
        total_now_num=0
        total_material_num=0
        material_reduce_rate_sum=0
        for tmp in res:
            all_material_map[tmp[0]] = (tmp[1], tmp[2])
            total_ori_num+=tmp[1]
            total_now_num+=tmp[2]
            try:
                material_reduce_rate_sum+=(tmp[1]-tmp[2])/tmp[1]
            except:
                continue
            total_material_num += 1

        sql = "select sum(in_num) from in_log"
        cur.execute(sql)
        res = cur.fetchone()
        total_in_num=res[0]
        if total_in_num is None:
            total_in_num=0

        sql = "select sum(out_num) from out_log"
        cur.execute(sql)
        res = cur.fetchone()
        total_out_num = res[0]
        if total_out_num is None:
            total_out_num=0

        cur.close()
        conn.close()

        self.lineEdit.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_6.setReadOnly(True)
        self.textEdit.setReadOnly(True)

        self.lineEdit.setText(str(round(total_ori_num,4)))
        self.lineEdit_2.setText(str(round(total_in_num,4)))
        self.lineEdit_3.setText(str(round(total_out_num,4)))
        self.lineEdit_4.setText(str(round(total_now_num,4)))

        total_reduce_num=round(total_ori_num-total_now_num,4)
        try:
            total_reduce_rate=total_reduce_num/total_ori_num
            self.lineEdit_5.setText(str(total_reduce_num) + '/' + str(round(total_reduce_rate * 100, 2)) + '%')
            self.lineEdit_6.setText(str(round(material_reduce_rate_sum / total_material_num * 100, 2)) + '%')
        except:
            total_reduce_rate='无效，期初总量等于0'
            self.lineEdit_5.setText(str(total_reduce_num) + '/' + total_reduce_rate)
            self.lineEdit_6.setText("无效，期初总量等于0")





    def on_cancel_btn_clicked(self):
        self.close()