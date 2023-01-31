import sqlite3

class Material():
    def __init__(self, material_id, name, spec, unit, per_price,position,ori_num, now_num):
        self.material_id = material_id
        self.material_name = name
        self.spec = spec
        self.unit = unit
        self.ori_num = ori_num
        self.now_num = now_num
        self.per_price = per_price
        self.position=position


    def insert_new_material(self):
        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        sql = "insert into material values('" + self.material_id + "','" + self.material_name + "','" + self.spec + "','" + self.unit + "',"+self.per_price+",'" +self.position+"',"+ self.ori_num + "," + self.now_num + ");"
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()


class In_Log():
    def __init__(self, date_time, material_id, name, spec, in_num, per_price,position,total_price,user_man, agree_man):
        self.date_time = date_time
        self.material_id = material_id
        self.material_name = name
        self.spec = spec
        self.in_num = in_num
        self.per_price=per_price
        self.position=position
        self.total_price=total_price
        self.user_man = user_man
        self.agree_man = agree_man

    def new_in_log(self):
        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        sql = "insert into in_log values(" + self.date_time + ",'" + self.material_id + "','" + self.material_name + "','" + self.spec + "'," + self.in_num + ","+self.per_price+",'"+self.position+"',"+self.total_price+",'" + self.user_man + "','" + self.agree_man + "', null);"
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()


class Out_Log():
    def __init__(self, date_time, material_id, name, spec, out_num, per_price,position,total_price,user_man, agree_man):
        self.date_time = date_time
        self.material_id = material_id
        self.material_name = name
        self.spec = spec
        self.out_num = out_num
        self.per_price=per_price
        self.position=position
        self.total_price=total_price
        self.user_man = user_man
        self.agree_man = agree_man

    def new_out_log(self):
        conn = sqlite3.connect("material_management.db")
        conn.text_factory = str
        cur = conn.cursor()
        sql = "insert into out_log values(" + self.date_time + ",'" + self.material_id + "','" + self.material_name + "','" + self.spec + "'," + self.out_num + ","+self.per_price+",'"+self.position+"',"+self.total_price+",'" + self.user_man + "','" + self.agree_man + "', null);"
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
