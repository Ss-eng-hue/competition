import time
from body import *


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


def log_in(username,password,root):  # 登录函数
    global login_time
    cursor.execute('select 账号 from 管理员')
    users = cursor.fetchall()
    ls = []
    for i in users:
        ls.append(i[0])
    a = username.get()
    b = password.get()
    if a in ls:
        cursor.execute('select 密码 from 管理员 where 账号="%s"' % a)
        pw = cursor.fetchall()
        if b == pw[0][0]:
            messagebox.showinfo(title='提示', message='登录成功')
            root.destroy()
            login_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            new(username, login_time)
        else:
            messagebox.showwarning(title='提示', message='密码错误')
    else:
        messagebox.showwarning(title='提示', message='账号错误')


def sign_window(root):  # 注册窗口
    global sign_root, var_use, var_password
    sign_root = Toplevel(root)
    sign_root.title("注册")
    sign_root.iconbitmap('../pic/图标.ico')
    sign_root.resizable(0, 0)
    sign_root.geometry("400x320+500+100")
    sign_root['bg'] = 'DeepSkyBlue'
    Pane_sign = PanedWindow(sign_root, width=390, height=300)
    Pane_sign.place(x=5, y=8)
    # 账号
    Label_user = Label(Pane_sign, text='账号：', font=('微软雅黑', 14))
    Label_user.place(x=80, y=50)
    var_use = StringVar()
    Entry_user = Entry(Pane_sign, textvariable=var_use, font=("微软雅黑", 14), width=16)
    Entry_user.place(x=140, y=52)
    # 密码
    Label_password = Label(Pane_sign, text='密码：', font=("微软雅黑", 14))
    Label_password.place(x=80, y=120)
    var_password = StringVar()
    Entry_password = Entry(Pane_sign, textvariable=var_password, font=("微软雅黑", 14), width=16)
    Entry_password.place(x=140, y=122)
    # 按钮
    Button(
        Pane_sign, text='确定', font=('华文行楷', 15),
        command=lambda: save_sign(var_use, var_password, sign_root)
    ).place(x=120, y=210)
    Button(Pane_sign, text='返回', font=('华文行楷', 15), command=lambda: close_sign(sign_root)).place(x=230, y=210)
