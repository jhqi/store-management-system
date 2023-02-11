import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
import resources_rc
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from update_material import Ui_update_material
import sqlite3


class update_material_window(QMainWindow, Ui_update_material):
    def __init__(self, tid):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.main_window = self
        self.setWindowIcon(QIcon(":/images/image.ico"))
        self.tid=tid
        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        sql = "select * from material where material_id='" + self.tid + "'"
        cur.execute(sql)
        res = cur.fetchone()
        cur.close()
        conn.close()
        self.material_id_lineEdit.setText(res[0])
        self.ori_id = res[0]
        self.material_name_lineEdit.setText(res[1])
        self.spec_lineEdit.setText(res[2])
        self.unit_lineEdit.setText(res[3])
        if res[4] == -1:
            per_price_content = '未知'
        else:
            per_price_content = str(res[4])
        self.per_price_lineEdit.setText(per_price_content)
        self.position_lineEdit.setText(res[5])
        self.ori_num_lineEdit.setText(str(res[6]))
        self.now_num_lineEdit.setText(str(res[7]))

        self.cancel_pushButton.clicked.connect(self.on_cancel_btn_clicked)
        # self.only_material_pushButton.clicked.connect(self.on_only_material_confirm_btn_clicked)
        self.both_confirm_pushButton.clicked.connect(self.on_both_btn_clicked)

    # 让多窗口之间传递信号 刷新主窗口信息
    my_Signal = QtCore.pyqtSignal()

    def sendEditContent(self):
        self.my_Signal.emit()

    def closeEvent(self, event):
        self.sendEditContent()

    def on_cancel_btn_clicked(self):
        self.close()

    # def on_only_material_confirm_btn_clicked(self):
    #     id=self.material_id_lineEdit.text()
    #     name=self.material_name_lineEdit.text()
    #     spec=self.spec_lineEdit.text()
    #     unit=self.unit_lineEdit.text()
    #     ori_num=self.ori_num_lineEdit.text()
    #     now_num=self.now_num_lineEdit.text()
    #
    #     conn = sqlite3.connect("material_management.db")
    #     conn.text_factory = str
    #     cur = conn.cursor()
    #     sql="select material_id from material"
    #     cur.execute(sql)
    #     res=cur.fetchall()
    #     id_list=[]
    #     for tmp in res:
    #         id_list.append(tmp[0])
    #     if id in id_list and id!=self.ori_id:
    #         QMessageBox.question(self, '更新失败！', '新物料编码与其他物料冲突！', QMessageBox.Yes)
    #         return
    #     sql="update material set material_id='"+id+"', material_name='"+name+"', spec='"+spec+"', unit='"+unit+"', ori_num="+ori_num+", now_num="+now_num+" where material_id='"+self.ori_id+"'"
    #     cur.execute(sql)
    #     conn.commit()
    #     cur.close()
    #     conn.close()
    #     QMessageBox.question(self, '更新成功！', '已修改对应物料！', QMessageBox.Yes)
    #     self.close()

    def on_both_btn_clicked(self):
        id = self.material_id_lineEdit.text()
        id = id.strip("\n\t ")
        if id == "":
            QMessageBox.question(self, '更新失败！', '存货编码不可为空！', QMessageBox.Yes)
            return
        name = self.material_name_lineEdit.text()
        name = name.strip("\n\t ")
        if name == "":
            QMessageBox.question(self, '更新失败！', '存货名称不可为空！', QMessageBox.Yes)
            return
        spec = self.spec_lineEdit.text()
        spec = spec.strip("\n\t ")
        if spec == "":
            QMessageBox.question(self, '更新失败！', '规格型号不可为空！', QMessageBox.Yes)
            return
        unit = self.unit_lineEdit.text()
        unit = unit.strip("\n\t ")
        if unit == "":
            QMessageBox.question(self, '更新失败！', '计量单位不可为空！', QMessageBox.Yes)
            return
        per_price = self.per_price_lineEdit.text()
        if per_price == "" or per_price == '未知':
            per_price = "-1"
        else:
            try:
                t = float(per_price)
            except:
                QMessageBox.question(self, '更新失败！', '单价应是实数！', QMessageBox.Yes)
                return

        position = self.position_lineEdit.text()
        position = position.strip("\n\t ")
        if position == "":
            position = "未知"

        ori_num = self.ori_num_lineEdit.text()
        if ori_num == "":
            QMessageBox.question(self, '更新失败！', '期初数量不可为空！', QMessageBox.Yes)
            return
        try:
            t = float(ori_num)
        except:
            QMessageBox.question(self, '更新失败！', '期初数量应是实数！', QMessageBox.Yes)
            return

        now_num = self.now_num_lineEdit.text()
        if now_num == "":
            QMessageBox.question(self, '更新失败！', '期初数量不可为空！', QMessageBox.Yes)
            return
        try:
            t = float(now_num)
        except:
            QMessageBox.question(self, '更新失败！', '结存数量应是实数！', QMessageBox.Yes)
            return

        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        sql = "update material set material_id='" + id + "',material_name='" + name + "',spec='" + spec + "',unit='" + unit + "',per_price=" + per_price + ",pos='" + position + "',ori_num=" + ori_num + ", now_num=" + now_num + " where material_id='" + self.ori_id + "'"
        try:
            cur.execute(sql)
        except:
            QMessageBox.question(self, '更新失败！', '新存货编码与已有物料重复！', QMessageBox.Yes)
            cur.close()
            conn.close()
            return
        sql = "update in_log set material_id='" + id + "', material_name='" + name + "', spec='" + spec + "',per_price=" + per_price + ",pos='" + position + "', total_price=in_num*" + str(
            per_price) + " where material_id='" + self.ori_id + "'"
        cur.execute(sql)
        sql = "update out_log set material_id='" + id + "', material_name='" + name + "', spec='" + spec + "',per_price=" + per_price + ",pos='" + position + "', total_price=out_num*" + str(
            per_price) + " where material_id='" + self.ori_id + "'"
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        QMessageBox.question(self, '更新成功！', '物料及对应出/入库信息已修改！', QMessageBox.Yes)
        self.close()
