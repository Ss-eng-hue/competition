import time
from tkinter import *
from tkinter import messagebox
import login
import my_sql

cursor = my_sql.cursor
root = Tk()  # 创建Tk控件
root.title("登录界面")  # 窗口标题
root.iconbitmap('../pic/图标.ico')  # 窗口图标
root.geometry("620x420+400+150")  # 窗口大小
root.resizable(0, 0)  # 窗体大小不允许变，两个参数分别代表x轴和y轴
root["bg"] = "DeepSkyBlue"  # 背景颜色
# 创建一个Label标签展示图片并设为背景

photo = PhotoImage(file= "../pic/登录.png")
image_lable = Label(root, image=photo, text='\t\t大数据与人工智能学院\n\n\t\t\t民宿管理系统',
                    justify=LEFT, compound=CENTER, font=('华文行楷', 26))
image_lable.pack(padx=10, pady=10)


def login():  # 登录函数
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
        else:
            messagebox.showwarning(title='提示', message='密码错误')
    else:
        messagebox.showwarning(title='提示', message='账号错误')


def sign_window():  # 注册窗口
    global sign_root, var_use, var_password
    sign_root = Toplevel(root)
    sign_root.title("注册")
    sign_root.iconbitmap('图标.ico')
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
    #TODO 报错无法控制
    Button(Pane_sign, text='确定', font=('华文行楷', 15),
           command=lambda: login.save_sign(var_use, var_password, sign_root)).place(x=120, y=210)
    Button(Pane_sign, text='返回', font=('华文行楷', 15), command=lambda: login.close_sign(sign_root)).place(x=230, y=210)


# 登录界面 用户名
user_lable = Label(root, text="用户名:", font=('华文行楷', 16))
user_lable.pack(side=LEFT, padx=10, pady=10)
username = StringVar()
user_entry = Entry(root, textvariable=username, width=10, font=('微软雅黑', 14))
user_entry.pack(side=LEFT, padx=10, pady=10)
# 密码
password_lable = Label(root, text="密码:", font=('华文行楷', 16))
password_lable.pack(side=LEFT, padx=10, pady=10)
password = StringVar()
password_entry = Entry(root, textvariable=password, width=10, show="*", font=('微软雅黑', 14))
password_entry.pack(side=LEFT, padx=10, pady=10)
# 按钮
login_bt = Button(root, text="登录", width=4, font=('华文行楷', 16), command=login)
login_bt.pack(side=RIGHT, padx=20, pady=10)
clear_bt = Button(root, text='注册', width=4, font=('华文行楷', 16), command=sign_window)
clear_bt.pack(side=RIGHT, padx=20, pady=10)

mainloop()
