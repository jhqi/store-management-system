import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
import resources_rc
from PyQt5.QtGui import QIcon
from objects import Material
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from new_material import Ui_new_material


class new_material_window(QMainWindow, Ui_new_material):
    def on_confirm_btn_clicked(self):
        material_id = self.material_id_lineEdit.text()
        material_id = material_id.strip("\n \t")
        if material_id == "":
            QMessageBox.question(self, '新增失败！', '存货编码不可为空！', QMessageBox.Yes)
            return
        material_name = self.material_name_lineEdit.text()
        material_name = material_name.strip("\n \t")
        if material_name == "":
            QMessageBox.question(self, '新增失败！', '存货名称不可为空！', QMessageBox.Yes)
            return
        spec = self.spec_lineEdit.text()
        spec = spec.strip("\n \t")
        if spec == "":
            QMessageBox.question(self, '新增失败！', '规格型号不可为空！', QMessageBox.Yes)
            return
        unit = self.unit_lineEdit.text()
        unit = unit.strip("\n \t")
        if unit == "":
            QMessageBox.question(self, '新增失败！', '计量单位不可为空！', QMessageBox.Yes)
            return
        per_price = self.per_price_lineEdit.text()
        if per_price == "" or per_price == '未知':
            per_price = float("-1")
        else:
            try:
                per_price = float(per_price)
            except:
                QMessageBox.question(self, '新增失败！', '单价应是实数！', QMessageBox.Yes)
        position = self.position_lineEdit.text()
        position = position.strip("\n \t")
        if position == "":
            position = "未知"
        ori_num = self.ori_num_lineEdit.text()
        if ori_num == "":
            QMessageBox.question(self, '新增失败！', '期初数量不可为空！', QMessageBox.Yes)
            return
        try:
            ori_num = float(ori_num)
        except:
            QMessageBox.question(self, '新增失败！', '期初数量必须为实数！', QMessageBox.Yes)
            return

        now_num = ori_num
        tmp_material = Material(material_id, material_name, spec, unit, str(per_price), position, str(ori_num),
                                str(now_num))
        try:
            tmp_material.insert_new_material()
            QMessageBox.question(self, '新增成功！', '新存货信息已录入！', QMessageBox.Yes)
            self.material_name_lineEdit.setText("")
            self.material_id_lineEdit.setText("")
            self.spec_lineEdit.setText("")
            self.unit_lineEdit.setText("")
            self.per_price_lineEdit.setText("")
            self.position_lineEdit.setText("")
            self.ori_num_lineEdit.setText("")
        except:
            QMessageBox.question(self, '新增失败！', '重复，库中已存在该存货编码！', QMessageBox.Yes)

    def on_cancel_btn_clicked(self):
        self.close()

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.main_window = self
        self.setWindowIcon(QIcon(":/images/image.ico"))
        self.confirm_pushButton.clicked.connect(self.on_confirm_btn_clicked)
        self.cancel_pushButton.clicked.connect(self.on_cancel_btn_clicked)
