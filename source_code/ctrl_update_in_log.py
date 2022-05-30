import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
import resources_rc
from PyQt5.QtGui import QIcon
import sqlite3
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from update_in_log import Ui_update_in_log
import var
from objects import Out_Log


class update_in_log_window(QMainWindow, Ui_update_in_log):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.main_window = self
        self.setWindowIcon(QIcon(":/images/image.ico"))
        self.both_btn.clicked.disconnect()
        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        sql = "select * from in_log where in_log_id=" + var.tin_log_id
        cur.execute(sql)
        res = cur.fetchone()
        cur.close()
        conn.close()

        tdate = res[0]
        t_year = tdate // 10000
        t_month = tdate % 10000 // 100
        t_day = tdate % 100

        self.ori_in_log_id = var.tin_log_id
        self.dateEdit.setDate(QDate(t_year, t_month, t_day))
        self.material_id_lineEdit.setText(res[1])
        self.material_name_lineEdit.setText(res[2])
        self.spec_lineEdit.setText(res[3])
        self.num_lineEdit.setText(str(res[4]))
        self.ori_in_num = res[4]
        per_price = res[5]
        if per_price == -1:
            per_price = '未知'
        else:
            per_price = str(per_price)
        self.per_price_lineEdit.setText(per_price)
        self.position_lineEdit.setText(res[6])

        self.user_lineEdit.setText(res[8])
        self.agree_lineEdit.setText(res[9])
        self.comboBox.setCurrentIndex(0)

        self.material_id_lineEdit.setReadOnly(True)
        self.material_name_lineEdit.setReadOnly(True)
        self.spec_lineEdit.setReadOnly(True)

        self.cancel_pushButton.clicked.connect(self.on_cancel_btn_clicked)
        self.both_btn.clicked.connect(self.on_both_btn_clicked)

    # 让多窗口之间传递信号 刷新主窗口信息
    my_Signal = QtCore.pyqtSignal()

    def sendEditContent(self):
        self.my_Signal.emit()

    def closeEvent(self, event):
        self.sendEditContent()

    def on_comfirm_btn_clicked(self):
        self.update_log()
        QMessageBox.question(self, '修改成功！', '1条入库记录已更新！', QMessageBox.Yes)
        self.close()

    def on_both_btn_clicked(self):
        try:
            self.now_num = float(self.num_lineEdit.text())
        except:
            QMessageBox.question(self, '修改失败！', '操作数量应是实数！', QMessageBox.Yes)

        tid = self.material_id_lineEdit.text()
        tid = tid.strip("\n\t ")
        if self.comboBox.currentIndex() == 1:  # 变成了出库
            self.now_num *= -1

        incr = self.now_num - self.ori_in_num
        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        sql = "select now_num from material where material_id='" + tid + "'"
        cur.execute(sql)
        res = cur.fetchone()
        cur.close()
        conn.close()
        new_now_num = res[0] + incr
        if new_now_num < 0:
            QMessageBox.question(self, '修改失败！', '结存数量小于0，库存不足！', QMessageBox.Yes)
            return
        flag = self.update_log()
        if flag == 0:
            return
        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        sql = "update material set now_num=" + str(new_now_num) + " where material_id='" + tid + "'"
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        QMessageBox.question(self, '修改成功！', '入库记录及对应存货的库存余量同时修改！', QMessageBox.Yes)
        self.close()

    def update_log(self):
        log_date = self.dateEdit.date().toString(Qt.ISODate)
        ll = log_date.split('-')
        log_date = "".join(ll)
        id = self.material_id_lineEdit.text()
        id = id.strip('\n\t ')
        name = self.material_name_lineEdit.text()
        name = name.strip('\n\t ')
        spec = self.spec_lineEdit.text()
        spec = spec.strip('\n\t ')
        num = self.num_lineEdit.text()
        if num == "":
            QMessageBox.question(self, '修改失败！', '操作数量不可为空！', QMessageBox.Yes)
            return 0
        try:
            t = float(num)
        except:
            QMessageBox.question(self, '修改失败！', '操作数量应是实数！', QMessageBox.Yes)
            return 0
        per_price = self.per_price_lineEdit.text()
        if per_price == '' or per_price == '未知':
            per_price = '-1'
            total_price = '-1'
        else:
            try:
                t = float(per_price)
                total_price = str(t * float(num))
            except:
                QMessageBox.question(self, '修改失败！', '单价应是实数！', QMessageBox.Yes)
                return 0
        position = self.position_lineEdit.text()
        position = position.strip('\n\t ')
        if position == '':
            position = '未知'
        user_man = self.user_lineEdit.text()
        user_man = user_man.strip('\n\t ')
        if user_man == "":
            user_man = '未知'
        agree_man = self.agree_lineEdit.text()
        agree_man = agree_man.strip('\n\t ')
        if agree_man == "":
            QMessageBox.question(self, '修改失败！', '令号不可为空！', QMessageBox.Yes)
            return 0

        if self.comboBox.currentIndex() == 0:  # 还是入库
            conn = sqlite3.connect("material_management.db")
            conn.text_factory = str
            cur = conn.cursor()
            sql = "update in_log set date_time=" + log_date + ",in_num=" + num + ", per_price=" + per_price + ", pos='" + position + "', total_price=" + total_price + ", user_man='" + user_man + "', agree_man='" + agree_man + "' where in_log_id=" + self.ori_in_log_id
            cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()
        else:  # 变成了出库
            conn = sqlite3.connect("material_management.db")
            conn.text_factory = str
            cur = conn.cursor()
            sql = "delete from in_log where in_log_id=" + self.ori_in_log_id
            cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()

            t_out_log = Out_Log(log_date, id, name, spec, num, per_price, position, total_price, user_man, agree_man)
            t_out_log.new_out_log()
        return 1

    def on_cancel_btn_clicked(self):
        self.close()
