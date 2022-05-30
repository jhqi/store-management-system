import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
import resources_rc
from PyQt5.QtGui import QIcon
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from clear_confirm import Ui_clear_confirm
import var


class clear_confirm_window(QMainWindow, Ui_clear_confirm):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.main_window = self
        self.confirm_btn.clicked.disconnect()
        self.cancel_btn.clicked.disconnect()
        self.setWindowIcon(QIcon(":/images/image.ico"))
        self.confirm_btn.clicked.connect(self.on_confirm_btn_clicked)
        self.cancel_btn.clicked.connect(self.on_cancel_btn_clicked)
        if var.clear_flag == 1:
            self.label.setText("警告！  确认清空所有存货数据？？")
            self.label_2.setText("将要删除存货数据！")
            self.label_2.setStyleSheet('background-color:red')
        elif var.clear_flag == 2:
            self.label.setText("警告！  确认清空所有入库数据？？")
            self.label_2.setText("将要删除入库数据！")
            self.label_2.setStyleSheet('background-color:red')
        else:
            self.label.setText("警告！  确认清空所有出库数据？？")
            self.label_2.setText("将要删除出库数据！")
            self.label_2.setStyleSheet('background-color:red')

    def on_confirm_btn_clicked(self):
        if var.clear_flag == 1:
            conn = sqlite3.connect("material_management.db")
            conn.text_factory = str
            cur = conn.cursor()
            sql = "drop table material"
            cur.execute(sql)
            conn.commit()
            cur.execute(
                "create table material(material_id varchar(32) primary key,material_name varchar(100),spec varchar(100),unit varchar(10), per_price float, pos varchar(100), ori_num float,now_num float)")
            conn.commit()
            cur.close()
            conn.close()
            QMessageBox.question(self, '删除成功！', '存货数据已全部删除！', QMessageBox.Yes)
        elif var.clear_flag == 2:
            conn = sqlite3.connect("material_management.db")
            conn.text_factory = str
            cur = conn.cursor()
            sql = "drop table in_log"
            cur.execute(sql)
            conn.commit()
            cur.execute(
                "create table in_log(date_time int,material_id varchar(32),material_name varchar(100),spec varchar(100),in_num float, per_price float, pos varchar(100), total_price float,user_man varchar(20),agree_man varchar(20), in_log_id INTEGER PRIMARY KEY AUTOINCREMENT)")

            conn.commit()
            cur.close()
            conn.close()
            QMessageBox.question(self, '删除成功！', '入库数据已全部删除！', QMessageBox.Yes)
        elif var.clear_flag == 3:
            conn = sqlite3.connect("material_management.db")
            conn.text_factory = str
            cur = conn.cursor()
            sql = "drop table out_log"
            cur.execute(sql)
            conn.commit()
            cur.execute(
                "create table out_log(date_time int,material_id varchar(32),material_name varchar(100),spec varchar(100),out_num float,per_price float, pos varchar(100), total_price float,user_man varchar(20),agree_man varchar(20), out_log_id INTEGER PRIMARY KEY AUTOINCREMENT)")

            conn.commit()
            cur.close()
            conn.close()
            QMessageBox.question(self, '删除成功！', '出库数据已全部删除！', QMessageBox.Yes)
        else:
            QMessageBox.question(self, '删除失败！', '未知错误！', QMessageBox.Yes)
        self.close()

    def on_cancel_btn_clicked(self):
        self.close()
