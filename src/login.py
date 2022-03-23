from tkinter import messagebox
import pymysql
from my_sql import connection
from my_sql import cursor

def save_sign(var_use, var_password, sign_root):  # 注册函数
    a = var_use.get()
    b = var_password.get()
    try:
        cursor.execute('insert into 管理员(账号,密码) values(%s,%s)', (a, b))
        connection.commit()
    except pymysql.DatabaseError:
        connection.rollback()
    else:
        messagebox.showinfo(title='提示', message='注册成功')
        sign_root.destroy()


def close_sign(sign_root):  # 关闭注册界面
    sign_root.destroy()
