# store-management-system
库房存货信息管理系统，使用python+pyqt5开发。可以新增存货，并对存货进行出入库管理。可以支持从excel导入入库出库单，也可以将信息导出至excel表格

# 使用说明
conda create -n py37 python=3.7

pip install openpyxl==2.3.5 -i https://pypi.douban.com/simple/

pip install pyqt5 -i https://pypi.douban.com/simple/

python main.py

# 功能
## 存货管理
新增、修改、删除、查询存货，对存货进行出、入库操作，支持批量操作

## 出/入库信息管理
修改、删除、查询出、入库记录
