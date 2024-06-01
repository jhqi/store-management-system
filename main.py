import sys
import os
import resources_rc
from sys import argv as SYS_argv
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import sqlite3
from home import Ui_home
from ctrl_new_material import new_material_window
from ctrl_material_in_out import material_in_log_window
from ctrl_material_info import material_info_window
from ctrl_in_info import in_info_window
from ctrl_out_info import out_info_window
from ctrl_clear_confirm import clear_confirm_window
from ctrl_import_confirm import import_confirm_window
from ctrl_lots_new import lots_new_window
from ctrl_lots_in_out import lots_in_out_window
from ctrl_total_data import total_data_window
from ctrl_shoufacun_info import shoufacun_info_window


class homeWindow(QMainWindow, Ui_home):
    def on_lots_in_out_btn_clicked(self):
        window = lots_in_out_window()
        window.show()

    def on_lots_new_material_btn_clicked(self):
        window=lots_new_window()
        window.show()

    def on_new_material_btn_clicked(self):
        window = new_material_window()
        window.show()

    def on_in_btn_clicked(self):
        window = material_in_log_window()
        window.show()

    def on_material_info_btn_clicked(self):
        # if self.material_info_btn_lock:
        #     return
        # self.material_info_btn_lock=True
        window = material_info_window()
        window.show()

    def on_in_info_btn_clicked(self):
        window = in_info_window()
        window.show()

    def on_out_info_btn_clicked(self):
        window = out_info_window()
        window.show()

    def on_del_material_btn_clicked(self):
        window = clear_confirm_window(clear_flag = 1)
        window.show()

    def on_del_in_btn_clicked(self):
        window = clear_confirm_window(clear_flag = 2)
        window.show()

    def on_del_out_btn_clicked(self):
        window = clear_confirm_window(clear_flag = 3)
        window.show()

    def on_import_material_btn_clicked(self):
        window = import_confirm_window(import_flag = 1)
        window.show()

    def on_import_in_log_btn_clicked(self):
        window = import_confirm_window(import_flag = 2)
        window.show()

    def on_import_out_log_btn_clicked(self):
        window = import_confirm_window(import_flag = 3)
        window.show()

    def on_total_data_btn_clicked(self):
        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        sql = "select count(*) from material"
        cur.execute(sql)
        res = cur.fetchone()
        if res[0] == 0:
            QMessageBox.question(self, '汇总统计失败！', '存货表为空！', QMessageBox.Yes)
            return
        window = total_data_window()
        window.show()

    def on_shoufacun_btn_clicked(self):
        window = shoufacun_info_window()
        window.show()

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowIcon(QIcon(':/images/image.ico'))
        self.in_info_btn.setStyleSheet("background:#FF95CA")
        self.clear_in_info_btn.setStyleSheet("background:#FF95CA")
        self.import_in_info_btn.setStyleSheet("background:#FF95CA")

        self.out_info_btn.setStyleSheet("background:#96FED1")
        self.clear_out_info_btn.setStyleSheet("background:#96FED1")
        self.import_out_info_btn.setStyleSheet("background:#96FED1")

        self.new_material_pushButton.setStyleSheet("background:#d0d0d0")
        self.lots_new_material_pushButton.setStyleSheet("background:#d0d0d0")
        self.total_data_btn.setStyleSheet("background:#d0d0d0")
        self.shoufacun_btn.setStyleSheet("background:#d0d0d0")
        self.material_info_btn.setStyleSheet("background:#d0d0d0")
        self.clear_material_btn.setStyleSheet("background:#d0d0d0")
        self.import_material_btn.setStyleSheet("background:#d0d0d0")

        self.in_material_pushButton.setStyleSheet("background:#FFFFAA")
        self.lots_pushButton.setStyleSheet("background:#BFCAE6")

        # 确认是否要建库
        flag = os.path.exists('material_management.db')
        if not flag:
            conn = sqlite3.connect("material_management.db")
            conn.text_factory = str
            cur = conn.cursor()

            cur.execute(
                "create table material(material_id varchar(256) primary key,material_name varchar(256),spec varchar(256),unit varchar(256), per_price float, pos varchar(256), ori_num float,now_num float)")

            cur.execute(
                "create table in_log(date_time int,material_id varchar(256),material_name varchar(256),spec varchar(256),in_num float, per_price float, pos varchar(256), total_price float,user_man varchar(256),agree_man varchar(256), in_log_id INTEGER PRIMARY KEY AUTOINCREMENT)")

            cur.execute(
                "create table out_log(date_time int,material_id varchar(256),material_name varchar(256),spec varchar(256),out_num float,per_price float, pos varchar(256), total_price float,user_man varchar(256),agree_man varchar(256), out_log_id INTEGER PRIMARY KEY AUTOINCREMENT)")

            conn.commit()
            cur.close()
            conn.close()

        # 解绑
        self.material_info_btn.clicked.disconnect()
        self.in_info_btn.clicked.disconnect()
        self.out_info_btn.clicked.disconnect()
        self.import_material_btn.clicked.disconnect()
        self.total_data_btn.clicked.disconnect()
        self.shoufacun_btn.clicked.disconnect()

        # self.import_in_info_btn.clicked.disconnect()
        # self.import_out_info_btn.clicked.disconnect()

        self.new_material_pushButton.clicked.connect(self.on_new_material_btn_clicked)
        self.in_material_pushButton.clicked.connect(self.on_in_btn_clicked)
        self.material_info_btn.clicked.connect(self.on_material_info_btn_clicked)
        self.in_info_btn.clicked.connect(self.on_in_info_btn_clicked)
        self.out_info_btn.clicked.connect(self.on_out_info_btn_clicked)
        self.clear_material_btn.clicked.connect(self.on_del_material_btn_clicked)
        self.clear_in_info_btn.clicked.connect(self.on_del_in_btn_clicked)
        self.clear_out_info_btn.clicked.connect(self.on_del_out_btn_clicked)
        self.import_material_btn.clicked.connect(self.on_import_material_btn_clicked)
        self.import_in_info_btn.clicked.connect(self.on_import_in_log_btn_clicked)
        self.import_out_info_btn.clicked.connect(self.on_import_out_log_btn_clicked)
        self.lots_pushButton.clicked.connect(self.on_lots_in_out_btn_clicked)
        self.lots_new_material_pushButton.clicked.connect(self.on_lots_new_material_btn_clicked)
        self.total_data_btn.clicked.connect(self.on_total_data_btn_clicked)
        self.shoufacun_btn.clicked.connect(self.on_shoufacun_btn_clicked)



    def closeEvent(self, event):
        event.accept()
        sys.exit(0)  # 退出程序


app = QApplication(SYS_argv)
window = homeWindow()
window.show()
os._exit(app.exec_())