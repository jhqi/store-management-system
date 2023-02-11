import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
import resources_rc
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from del_confirm import Ui_del_confirm


class del_confirm_window(QMainWindow, Ui_del_confirm):
    def __init__(self, del_type, del_num, del_ids, in_out_nums=None, material_ids=None):
        # del_type=1 #删除存货，及存货对应的入库、出库信息
        # del_type=2 #删除入库记录
        # del_type=3 #删除出库记录
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.main_window = self
        self.confirm_btn.clicked.disconnect()
        self.cancel_btn.clicked.disconnect()
        self.setWindowIcon(QIcon(":/images/image.ico"))
        self.confirm_btn.clicked.connect(self.on_confirm_btn_clicked)
        self.cancel_btn.clicked.connect(self.on_cancel_btn_clicked)

        self.del_type=del_type
        self.del_num=del_num
        self.del_ids=del_ids
        self.in_out_nums=in_out_nums
        self.material_ids=material_ids

        if self.del_type == 1:
            self.label.setText(f"警告！  确认删除{self.del_num}条存货数据？？")
            self.label_2.setText(f"将要删除{self.del_num}条存货数据！")
            self.label_2.setStyleSheet('background-color:red')
        elif self.del_type == 2:
            self.label.setText(f"警告！  确认删除{self.del_num}条入库数据？？")
            self.label_2.setText(f"将要删除{self.del_num}条入库数据！")
            self.label_2.setStyleSheet('background-color:red')
        else:
            self.label.setText(f"警告！  确认删除{self.del_num}条出库数据？？")
            self.label_2.setText(f"将要删除{self.del_num}条出库数据！")
            self.label_2.setStyleSheet('background-color:red')

    # 让多窗口之间传递信号 刷新主窗口信息
    del_finish_Signal = QtCore.pyqtSignal()

    def sendEditContent(self):
        self.del_finish_Signal.emit()

    def closeEvent(self, event):
        self.sendEditContent()

    def on_confirm_btn_clicked(self):
        if self.del_type == 1:

            conn = sqlite3.connect("material_management.db")
            conn.text_factory = str
            cur = conn.cursor()
            for tid in self.del_ids:
                sql = "delete from material where material_id='" + tid + "'"
                cur.execute(sql)
                sql = "delete from in_log where material_id='" + tid + "'"
                cur.execute(sql)
                sql = "delete from out_log where material_id='" + tid + "'"
                cur.execute(sql)
                conn.commit()
            cur.close()
            conn.close()
            QMessageBox.question(self, '删除成功！', str(self.del_num) + '条存货已删除！', QMessageBox.Yes)

        elif self.del_type == 2:
            conn = sqlite3.connect("material_management.db")
            conn.text_factory = str
            cur = conn.cursor()
            for i in range(0, self.del_num):
                sql = "select now_num from material where material_id='" + self.material_ids[i] + "'"
                cur.execute(sql)
                res = cur.fetchone()
                now_num = res[0]
                new_num = now_num - self.in_out_nums[i]
                if new_num < 0:
                    if self.del_num == 1:
                        QMessageBox.question(self, '删除失败！', '若删除该条入库记录，对应结存数量小于0！\n未执行删除！',
                                             QMessageBox.Yes)
                    else:
                        QMessageBox.question(self, '删除出错！', '成功删除前' + str(
                            i) + '条入库记录！\n' + '下一条入库记录若删除，对应结存数量小于0，停止删除！',
                                             QMessageBox.Yes)
                    cur.close()
                    conn.close()
                    self.close()
                    return
                sql = "update material set now_num=" + str(new_num) + " where material_id='" + self.material_ids[i] + "'"
                cur.execute(sql)
                sql = "delete from in_log where in_log_id=" + self.del_ids[i]
                cur.execute(sql)
                conn.commit()
            cur.close()
            conn.close()
            QMessageBox.question(self, '删除成功！', str(self.del_num) + '条入库记录已删除', QMessageBox.Yes)
        elif self.del_type == 3:
            conn = sqlite3.connect("material_management.db")
            conn.text_factory = str
            cur = conn.cursor()
            for i in range(0, self.del_num):
                sql = "select now_num from material where material_id='" + self.material_ids[i] + "'"
                cur.execute(sql)
                res = cur.fetchone()
                now_num = res[0]
                new_num = now_num + self.in_out_nums[i]
                sql = "update material set now_num=" + str(new_num) + " where material_id='" + self.material_ids[i] + "'"
                cur.execute(sql)
                sql = "delete from out_log where out_log_id=" + self.del_ids[i]
                cur.execute(sql)
                conn.commit()
            cur.close()
            conn.close()
            QMessageBox.question(self, '删除成功！', str(self.del_num) + '条出库记录已删除！', QMessageBox.Yes)
        else:
            QMessageBox.question(self, '删除失败！', '未知错误！', QMessageBox.Yes)
        self.close()

    def on_cancel_btn_clicked(self):
        self.close()
