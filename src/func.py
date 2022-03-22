# -*- coding: utf-8 -*-
# @Time    : 3/22/2022 10:33 AM
# @Author  : taltalasuka
# @File    : func.py
# @Software: PyCharm



from tkinter import messagebox
from tkinter.ttk import Treeview
from tkinter.ttk import Combobox
import time
import pymysql
from tkinter import *

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             database='民宿客房管理系统',
                             charset='utf8')
cursor = connection.cursor()  # 创建游标



def search_all():  # 显示全部
    item = Tree.get_children()
    for i in item:
        Tree.delete(i)
    cursor.execute('select * from 住房记录')
    info = cursor.fetchall()
    info_ls = []
    for i in info:
        info_ls.append(i)
    for i in range(len(info_ls)):
        Tree.insert("", i, values=(info_ls[i][0], info_ls[i][1], info_ls[i][2], info_ls[i][3],
                                   info_ls[i][5], info_ls[i][6], info_ls[i][7]))


def search():  # 查询函数
    item = Tree.get_children()
    for i in item:
        Tree.delete(i)
    a = Search_room.get()
    b = Search_name.get()
    c = Search_ID.get()
    info_ls = []
    if b == '' and c == '':
        cursor.execute('select * from 住房记录 where 房号=%s', a)
        info = cursor.fetchall()
        for i in info:
            info_ls.append(i)
    elif a == '' and c == '':
        cursor.execute('select * from 住房记录 where 姓名=%s', b)
        info = cursor.fetchall()
        for i in info:
            info_ls.append(i)
    elif a == '' and b == '':
        cursor.execute('select * from 住房记录 where 身份证号=%s', c)
        info = cursor.fetchall()
        for i in info:
            info_ls.append(i)
    elif a == '':
        cursor.execute('select * from 住房记录 where 姓名=%s and 身份证号=%s', (b, c))
        info = cursor.fetchall()
        for i in info:
            info_ls.append(i)
    elif b == '':
        cursor.execute('select * from 住房记录 where 房号=%s and 身份证号=%s', (a, c))
        info = cursor.fetchall()
        for i in info:
            info_ls.append(i)
    elif c == '':
        cursor.execute('select * from 住房记录 where 房号=%s and 姓名=%s', (a, b))
        info = cursor.fetchall()
        for i in info:
            info_ls.append(i)
    else:
        cursor.execute('select * from 住房记录 where 房号=%s and 姓名=%s and 身份证号=%s', (a, b, c))
        info = cursor.fetchall()
        for i in info:
            info_ls.append(i)
    for i in range(len(info_ls)):
        Tree.insert("", i, values=(info_ls[i][0], info_ls[i][1], info_ls[i][2], info_ls[i][3],
                                   info_ls[i][5], info_ls[i][6], info_ls[i][7]))


def save_data():  # 添加函数
    room = var_room.get()
    name = var_name.get()
    ID = var_ID.get()
    sex = var_sex.get()
    if sex == 1:
        a = '男'
    else:
        a = '女'
    nb = var_nb.get()
    in_time = var_in_time.get()
    out_time = var_out_time.get()
    room_typle = var_room_typle.get()
    days = var_days.get()
    cost = var_cost.get()
    native = var_native.get()
    try:
        cursor.execute('insert into 客户(姓名,性别,身份证号,籍贯,联系方式) values(%s,%s,%s,%s,%s)',
                       (name, a, ID, native, nb))
        cursor.execute('insert into 入住信息(入住时间,房号,退房时间,身份证号) values(%s,%s,%s,%s)',
                       (in_time, room, out_time, ID))
        cursor.execute('insert into 住房记录(房号,姓名,性别,身份证号,联系方式,入住时间,退房时间,房间类型,住房天数,消费,籍贯) '
                       'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       (room, name, a, ID, nb, in_time, out_time, room_typle, days, cost, native))
        connection.commit()
    except pymysql.DatabaseError:
        connection.rollback()
    else:
        messagebox.showinfo(title='提示', message='添加成功')
        data_root.destroy()
    search_all()


def change_data():  # 修改函数
    room = var_room.get()
    ID = var_ID.get()
    nb = var_nb.get()
    in_time = var_in_time.get()
    out_time = var_out_time.get()
    room_typle = var_room_typle.get()
    days = var_days.get()
    cost = var_cost.get()
    try:
        cursor.execute('update 客户 set 联系方式=%s where 身份证号=%s', (nb, ID))
        cursor.execute('update 入住信息 set 入住时间=%s,房号=%s,退房时间=%s where 身份证号=%s', (in_time, room, out_time, ID))
        cursor.execute('update 住房记录 set 房号=%s,联系方式=%s,入住时间=%s,退房时间=%s,房间类型=%s,住房天数=%s,消费=%s'
                       'where 身份证号=%s',
                       (room, nb, in_time, out_time, room_typle, days, cost, ID))
        connection.commit()
    except pymysql.DatabaseError:
        connection.rollback()
    else:
        messagebox.showinfo(title="提示", message="修改成功")
        data_root.destroy()
    search_all()


def show_close():  # 关闭明细窗口
    data_root.destroy()


def show_data(sign):  # 明细窗口
    global data_photo, data_root, var_room, var_name, var_ID, var_sex, var_nb, var_in_time, \
        var_out_time, var_room_typle, var_days, var_cost, var_native, var_user
    room_ls = []
    room_typle_ls = []
    room_cost_ls = []
    cursor.execute('select 房号 from 客房')
    ls_room = cursor.fetchall()
    for i in ls_room:
        room_ls.append(i[0])
    cursor.execute('select distinct(类型) from 客房')
    ls_typle = cursor.fetchall()
    for i in ls_typle:
        room_typle_ls.append(i[0])
    cursor.execute('select distinct(房价) from 客房')
    ls_cost = cursor.fetchall()
    for i in ls_cost:
        room_cost_ls.append(i[0])
    title_ls = ['添加信息', '修改信息', '查看信息']
    text_ls = ['==添加窗体==', '==修改窗体==', '==查看窗体==']
    data_root = Toplevel(user_root)
    if sign == '1':
        data_root.title(title_ls[0])
    elif sign == '2':
        data_root.title(title_ls[1])
    elif sign == '3':
        data_root.title(title_ls[2])
    data_root.geometry("600x500+600+150")
    data_root.iconbitmap('图标.ico')
    data_root.resizable(0, 0)  # 不能改变大小
    data_root['bg'] = 'DeepSkyBlue'
    # 添加图片
    data_photo = PhotoImage(file="明细窗口.png")
    data_image_lable = Label(data_root, image=data_photo)
    data_image_lable.pack()
    # 添加图片标题
    if sign == '1':
        Label_title = Label(data_root, text=text_ls[0], font=('华文行楷', 16))
        Label_title.place(x=380, y=20)
    elif sign == '2':
        Label_title = Label(data_root, text=text_ls[1], font=('华文行楷', 16))
        Label_title.place(x=380, y=20)
    elif sign == '3':
        Label_title = Label(data_root, text=text_ls[2], font=('华文行楷', 16))
        Label_title.place(x=380, y=20)
    # 加载一个文本块
    Pane_detail = PanedWindow(data_root, width=590, height=400)
    Pane_detail.place(x=5, y=88)
    # 添加属性
    # 第一排：下拉式房号
    Label_room = Label(Pane_detail, text="房间号：")
    Label_room.place(x=30, y=10)
    var_room = StringVar()
    Entry_room = Combobox(Pane_detail, textvariable=var_room, font=("微软雅黑", 14), width=10, value=room_ls)
    Entry_room.configure(state="readonly")
    Entry_room.place(x=110, y=8)
    # 姓名
    Label_name = Label(Pane_detail, text="姓名：")
    Label_name.place(x=260, y=10)
    var_name = StringVar()
    Entry_name = Entry(Pane_detail, textvariable=var_name, font=("微软雅黑", 14), width=10)
    Entry_name.place(x=310, y=8)
    # 第二排：身份证号
    Label_ID = Label(Pane_detail, text="身份证号:")
    Label_ID.place(x=30, y=60)
    var_ID = StringVar()
    Entry_ID = Entry(Pane_detail, textvariable=var_ID, font=("微软雅黑", 14), width=16)
    Entry_ID.place(x=110, y=58)
    # 性别
    Label_sex = Label(Pane_detail, text="性别:")
    Label_sex.place(x=310, y=60)
    var_sex = IntVar()
    Radio_man = Radiobutton(Pane_detail, text="男", variable=var_sex, value=1)
    Radio_man.place(x=360, y=60)
    Radio_woman = Radiobutton(Pane_detail, text="女", variable=var_sex, value=0)
    Radio_woman.place(x=410, y=60)
    # 第三排：联系方式
    Label_nb = Label(Pane_detail, text="联系方式:")
    Label_nb.place(x=30, y=110)
    var_nb = StringVar()
    Entry_nb = Entry(Pane_detail, textvariable=var_nb, font=("微软雅黑", 14), width=16)
    Entry_nb.place(x=110, y=108)
    # 籍贯
    Label_native = Label(Pane_detail, text="籍贯:")
    Label_native.place(x=310, y=110)
    var_native = StringVar()
    Entry_native = Combobox(Pane_detail, textvariable=var_native, font=("微软雅黑", 14), width=14)
    Entry_native['value'] = ['河北省', '山西省', '辽宁省', '吉林省', '黑龙江省', '江苏省', '浙江省', '安徽省', '福建省', '江西省',
                             '山东省', '河南省', '湖北省', '湖南省', '广东省', '海南省', '四川省', '贵州省', '云南省', '陕西省',
                             '甘肃省 ', '青海省', '台湾省', '内蒙古自治区', '广西壮族自治区', '西藏自治区', '宁夏回族自治区',
                             '新疆维吾尔自治区', '北京市', '天津市', '上海市', '重庆市', '香港特别行政区', '澳门特别行政区']
    Entry_native.configure(state="readonly")
    Entry_native.place(x=380, y=108)
    # 第四排：入住时间
    Label_in_time = Label(Pane_detail, text="入住时间:")
    Label_in_time.place(x=30, y=160)
    var_in_time = StringVar()
    Entry_in_time = Entry(Pane_detail, textvariable=var_in_time, font=("微软雅黑", 14), width=16)
    Entry_in_time.place(x=110, y=158)
    # 退房时间
    Label_out_time = Label(Pane_detail, text="退房时间:")
    Label_out_time.place(x=310, y=160)
    var_out_time = StringVar()
    Entry_out_time = Entry(Pane_detail, textvariable=var_out_time, font=("微软雅黑", 14), width=15)
    Entry_out_time.place(x=380, y=158)
    # 第五排：下拉式房间类型
    Label_room_typle = Label(Pane_detail, text="房间类型:")
    Label_room_typle.place(x=30, y=210)
    var_room_typle = StringVar()
    Entry_room_typle = Combobox(Pane_detail, textvariable=var_room_typle, font=("微软雅黑", 15),
                                width=14, value=room_typle_ls)
    Entry_room_typle.configure(state="readonly")
    Entry_room_typle.place(x=110, y=208)
    # 前台
    if sign == '3':
        Label_user = Label(Pane_detail, text="前台")
        Label_user.place(x=310, y=210)
        var_user = StringVar()
        Entry_user = Entry(Pane_detail, textvariable=var_user, font=("微软雅黑", 14), width=15)
        Entry_user.place(x=380, y=208)
    # 第六排：入住天数
    Label_days = Label(Pane_detail, text="入住天数:")
    Label_days.place(x=30, y=260)
    var_days = StringVar()
    Entry_days = Entry(Pane_detail, textvariable=var_days, font=("微软雅黑", 14), width=16)
    Entry_days.place(x=110, y=258)
    # 下拉式费用
    Label_cost = Label(Pane_detail, text="消费:")
    Label_cost.place(x=310, y=260)
    var_cost = StringVar()
    Entry_cost = Combobox(Pane_detail, textvariable=var_cost, font=("微软雅黑", 14), width=14, value=room_cost_ls)
    Entry_cost.place(x=380, y=258)
    # 按钮
    if sign == '1':
        Button_save_change = Button(data_root, text="保存", font=('华文行楷', 15), command=save_data)
        Button_save_change.place(x=400, y=420)
    elif sign == '2':
        Button_save_change = Button(data_root, text="修改", font=('华文行楷', 15), command=change_data)
        Button_save_change.place(x=400, y=420)
    Button(data_root, text="关闭", font=('华文行楷', 15), command=show_close).place(x=502, y=420)
    if sign == '2':
        Entry_name["state"] = DISABLED
        Entry_ID["state"] = DISABLED
        Radio_man["state"] = DISABLED
        Radio_woman["state"] = DISABLED
        Entry_native["state"] = DISABLED
    elif sign == '3':
        Entry_room["state"] = DISABLED
        Entry_name["state"] = DISABLED
        Entry_ID["state"] = DISABLED
        Radio_man["state"] = DISABLED
        Radio_woman["state"] = DISABLED
        Entry_nb["state"] = DISABLED
        Entry_in_time["state"] = DISABLED
        Entry_out_time["state"] = DISABLED
        Entry_room_typle["state"] = DISABLED
        Entry_days["state"] = DISABLED
        Entry_cost["state"] = DISABLED
        Entry_native["state"] = DISABLED
        Entry_user["state"] = DISABLED


def add_window():  # 添加窗口
    show_data('1')


def alter_window():  # 修改窗口
    ls = []
    item = Tree.selection()[0]
    show_data('2')
    info_list = Tree.item(item, "values")
    cursor.execute('select * from 住房记录 where 身份证号=%s', info_list[3])
    info = cursor.fetchall()
    for i in info:
        ls.append(i)
    var_room.set(ls[0][0])
    var_name.set(ls[0][1])
    if '男' in ls[0][2]:
        var_sex.set(1)
    else:
        var_sex.set(0)
    var_ID.set(ls[0][3])
    var_nb.set(ls[0][4])
    var_in_time.set(ls[0][5])
    var_out_time.set(ls[0][6])
    var_room_typle.set(ls[0][7])
    var_days.set(ls[0][8])
    var_cost.set(ls[0][9])
    var_native.set(ls[0][10])


def view_data(event):  # 双击窗口
    ls = []
    item = Tree.selection()[0]
    show_data('3')
    info_list = Tree.item(item, "values")
    cursor.execute('select * from 住房记录 where 身份证号=%s', info_list[3])
    info = cursor.fetchall()
    for i in info:
        ls.append(i)
    var_room.set(ls[0][0])
    var_name.set(ls[0][1])
    if '男' in ls[0][2]:
        var_sex.set(1)
    else:
        var_sex.set(0)
    var_ID.set(ls[0][3])
    var_nb.set(ls[0][4])
    var_in_time.set(ls[0][5])
    var_out_time.set(ls[0][6])
    var_room_typle.set(ls[0][7])
    var_days.set(ls[0][8])
    var_cost.set(ls[0][9])
    var_native.set(ls[0][10])
    var_user.set(ls[0][11])


def delete_data():  # 删除函数
    a = delete_room.get()
    b = delete_name.get()
    c = delete_ID.get()
    try:
        cursor.execute('delete from 客户 where 姓名=%s and 身份证号=%s ', (b, c))
        cursor.execute('delete from 入住信息 where 房号=%s and 身份证号=%s', (a, c))
        cursor.execute('delete from 住房记录 where 房号=%s and 姓名=%s and 身份证号=%s ', (a, b, c))
        connection.commit()
    except pymysql.DatabaseError:
        connection.rollback()
    else:
        messagebox.showinfo(title='提示', message='删除成功')
        delete_root.destroy()
    search_all()


def delete_close():  # 关闭删除窗口
    delete_root.destroy()


def delete_window():  # 删除窗口
    global delete_root, delete_photo, delete_room, delete_name, delete_ID
    delete_root = Toplevel(user_root)
    delete_root.title('删除信息')
    delete_root.iconbitmap('图标.ico')
    delete_root.geometry("600x400+600+150")
    delete_root.resizable(0, 0)  # 不能改变大小
    delete_root['bg'] = 'DeepSkyBlue'
    # 添加图片
    delete_photo = PhotoImage(file="明细窗口.png")
    delete_image_lable = Label(delete_root, image=delete_photo)
    delete_image_lable.pack()
    # 添加文本
    Label_title = Label(delete_root, text='==删除窗体==', font=('华文行楷', 16))
    Label_title.place(x=380, y=20)
    # 添加布局
    Pane_detail = PanedWindow(delete_root, width=590, height=300)
    Pane_detail.place(x=5, y=88)
    # 第一排：房间号
    Label_room = Label(Pane_detail, text="房间号：", font=("微软雅黑", 12))
    Label_room.place(x=160, y=15)
    delete_room = StringVar()
    Entry_room = Entry(Pane_detail, textvariable=delete_room, font=("微软雅黑", 14), width=16)
    Entry_room.place(x=260, y=13)
    # 第二排：姓名
    Label_name = Label(Pane_detail, text="姓名：", font=("微软雅黑", 12))
    Label_name.place(x=160, y=75)
    delete_name = StringVar()
    Entry_name = Entry(Pane_detail, textvariable=delete_name, font=("微软雅黑", 14), width=16)
    Entry_name.place(x=260, y=73)
    # 第三排：身份证号
    Label_ID = Label(Pane_detail, text="身份证号：", font=("微软雅黑", 12))
    Label_ID.place(x=160, y=135)
    delete_ID = StringVar()
    Entry_ID = Entry(Pane_detail, textvariable=delete_ID, font=("微软雅黑", 14), width=16)
    Entry_ID.place(x=260, y=133)

    ls = []
    item = Tree.selection()[0]
    info_list = Tree.item(item, "values")
    cursor.execute('select * from 住房记录 where 身份证号=%s', info_list[3])
    info = cursor.fetchall()
    for i in info:
        ls.append(i)
    delete_room.set(ls[0][0])
    delete_name.set(ls[0][1])
    delete_ID.set(ls[0][3])
    Entry_room["state"] = DISABLED
    Entry_name["state"] = DISABLED
    Entry_ID["state"] = DISABLED

    # 按钮
    Button(delete_root, text="删除", font=('华文行楷', 15), command=delete_data).place(x=235, y=300)
    Button(delete_root, text="关闭", font=('华文行楷', 15), command=delete_close).place(x=335, y=300)


def show_room():  # 显示房间信息
    item = room_Tree.get_children()
    for i in item:
        room_Tree.delete(i)
    cursor.execute('select * from 客房')
    info = cursor.fetchall()
    info_ls = []
    for i in info:
        info_ls.append(i)
    for i in range(len(info_ls)):
        room_Tree.insert("", i, values=(info_ls[i][0], info_ls[i][1], info_ls[i][2]))


def save_room_data():  # 保存房间数据
    a = room_id.get()
    b = room_mold.get()
    c = room_cost.get()
    if a != '' and b != '' and c != '':
        try:
            cursor.execute('insert into 客房(房号,类型,房价) values(%s,%s,%s)', (a, b, c))
            connection.commit()
        except pymysql.DatabaseError:
            connection.rollback()
        else:
            messagebox.showinfo(title='提示', message='添加成功')
            add_alter_root.destroy()
    else:
        messagebox.showwarning(title='提示', message='信息不能为空')
    show_room()


def alter_room_data():  # 修改房间数据
    a = room_id.get()
    b = room_mold.get()
    c = room_cost.get()
    if a != '' and b != '' and c != '':
        try:
            cursor.execute('update 客房 set 类型=%s,房价=%s where 房号=%s', (b, c, a))
            connection.commit()
        except pymysql.DatabaseError:
            connection.rollback()
        else:
            messagebox.showinfo(title='提示', message='修改成功')
            add_alter_root.destroy()
    else:
        messagebox.showwarning(title='提示', message='信息不能为空')
    show_room()


def remove_room_data():  # 删除房间
    a = room_id.get()
    try:
        cursor.execute('delete from 客房 where 房号=%s', a)
        connection.commit()
    except pymysql.DatabaseError:
        connection.rollback()
    else:
        messagebox.showinfo(title='提示', message='删除成功')
        add_alter_root.destroy()
    show_room()


def close_add_alter_room_window():  # 关闭房间明细窗口
    add_alter_root.destroy()


def add_alter_room_window(sign):  # 管理房间窗口
    global add_alter_root, room_id, room_mold, room_cost
    add_alter_root = Toplevel(room_root)
    if sign == '1':
        add_alter_root.title("添加客房")
    elif sign == '2':
        add_alter_root.title("修改客房")
    elif sign == '3':
        add_alter_root.title("删除客房")
    add_alter_root.geometry("400x300+900+100")
    add_alter_root.iconbitmap('图标.ico')
    add_alter_root.resizable(0, 0)
    add_alter_root['bg'] = 'DeepSkyBlue'
    Pane_room = PanedWindow(add_alter_root, width=390, height=280)
    Pane_room.place(x=5, y=8)
    # 房号
    Label_room_id = Label(Pane_room, text='房号：', font=('微软雅黑', 14))
    Label_room_id.place(x=75, y=40)
    room_id = StringVar()
    Entry_room_id = Entry(Pane_room, textvariable=room_id, font=("微软雅黑", 14), width=16)
    Entry_room_id.place(x=140, y=42)
    # 类型
    Label_room_typle = Label(Pane_room, text='类型：', font=("微软雅黑", 14))
    Label_room_typle.place(x=75, y=100)
    room_mold = StringVar()
    Entry_room_typle = Entry(Pane_room, textvariable=room_mold, font=("微软雅黑", 14), width=16)
    Entry_room_typle.place(x=140, y=102)
    # 房价
    Label_room_cost = Label(Pane_room, text='房价：', font=("微软雅黑", 14))
    Label_room_cost.place(x=75, y=160)
    room_cost = StringVar()
    Entry_room_cost = Entry(Pane_room, textvariable=room_cost, font=("微软雅黑", 14), width=16)
    Entry_room_cost.place(x=140, y=162)
    # 按钮
    if sign == '1':
        Button(Pane_room, text='确定', font=('华文行楷', 15), command=save_room_data).place(x=120, y=230)
    elif sign == '2':
        Button(Pane_room, text='修改', font=('华文行楷', 15), command=alter_room_data).place(x=120, y=230)
        Entry_room_id['state'] = DISABLED
    elif sign == '3':
        Button(Pane_room, text='删除', font=('华文行楷', 15), command=remove_room_data).place(x=120, y=230)
        Entry_room_id['state'] = DISABLED
        Entry_room_typle['state'] = DISABLED
        Entry_room_cost['state'] = DISABLED
    Button(Pane_room, text='返回', font=('华文行楷', 15), command=close_add_alter_room_window).place(x=230, y=230)


def add_room():  # 添加房间
    add_alter_room_window('1')


def alter_room():  # 修改房间
    item = room_Tree.selection()[0]
    add_alter_room_window('2')
    info_list = room_Tree.item(item, "values")
    room_id.set(info_list[0])
    room_mold.set(info_list[1])
    room_cost.set(info_list[2])


def remove_room():  # 删除房间
    item = room_Tree.selection()[0]
    add_alter_room_window('3')
    info_list = room_Tree.item(item, "values")
    room_id.set(info_list[0])
    room_mold.set(info_list[1])
    room_cost.set(info_list[2])


def close_room_window():  # 关闭管理房间窗口
    room_root.destroy()


def room_window():  # 管理窗口
    global room_root, room_Tree
    room_root = Toplevel(user_root)
    room_root.title("管理客房")
    room_root.iconbitmap('图标.ico')
    room_root.resizable(0, 0)
    room_root.geometry("600x400+800+200")
    room_root['bg'] = 'DeepSkyBlue'
    # 左侧按钮块
    Pane_room_left = PanedWindow(room_root, width=190, height=380)
    Pane_room_left.place(x=5, y=8)
    Button(Pane_room_left, text="显示全部", font=('华文行楷', 15), command=show_room).place(x=50, y=20)
    Button(Pane_room_left, text="添加客房", font=('华文行楷', 15), command=add_room).place(x=50, y=70)
    Button(Pane_room_left, text="修改客房", font=('华文行楷', 15), command=alter_room).place(x=50, y=120)
    Button(Pane_room_left, text="删除客房", font=('华文行楷', 15), command=remove_room).place(x=50, y=170)
    Button(Pane_room_left, text="关        闭", font=('华文行楷', 15), command=close_room_window).place(x=50, y=220)
    # 右侧展示块
    Pane_room_right = PanedWindow(room_root, width=390, height=380)
    Pane_room_right.place(x=200, y=8)
    # 添加Treeview控件
    room_Tree = Treeview(room_root, columns=("room_id", "room_typle", "room_cost"), show="headings", height=17)
    # 设置每一个列的宽度和对齐的方式
    room_Tree.column("room_id", width=120, anchor="center")
    room_Tree.column("room_typle", width=120, anchor="center")
    room_Tree.column("room_cost", width=120, anchor="center")
    # 设置每个列的标题
    room_Tree.heading("room_id", text="房号")
    room_Tree.heading("room_typle", text="类型")
    room_Tree.heading("room_cost", text="房价")
    # 添加
    room_Tree.place(x=214, y=15)


def save_change_password():  # 修改密码函数
    a = var_zh.get()
    b = var_pwd.get()
    c = var_pwd_again.get()
    if b != '' and c != '':
        if b == c:
            try:
                cursor.execute('update 管理员 set 密码=%s where 账号=%s', (c, a))
                connection.commit()
            except pymysql.DatabaseError:
                connection.rollback()
            else:
                messagebox.showinfo(title='提示', message='密码已修改')
                password_root.destroy()
        else:
            messagebox.showwarning(title='提示', message='密码不一致')
    else:
        messagebox.showwarning(title='提示', message='密码不能为空')


def close_change_password_window():  # 关闭修改密码窗口
    password_root.destroy()


def change_password_window():  # 修改密码窗口
    global password_root, var_zh, var_pwd, var_pwd_again
    password_root = Toplevel(user_root)
    password_root.title("修改密码")
    password_root.iconbitmap('图标.ico')
    password_root.resizable(0, 0)
    password_root.geometry("400x320+800+200")
    password_root['bg'] = 'DeepSkyBlue'
    Pane_password = PanedWindow(password_root, width=390, height=300)
    Pane_password.place(x=5, y=8)
    # 账号
    Label_pwd = Label(Pane_password, text='账号：', font=('微软雅黑', 14))
    Label_pwd.place(x=75, y=40)
    var_zh = StringVar()
    var_zh.set(username.get())
    Entry_pwd = Entry(Pane_password, textvariable=var_zh, font=("微软雅黑", 14), width=16)
    Entry_pwd.place(x=140, y=42)
    Entry_pwd["state"] = DISABLED
    # 密码
    Label_pwd = Label(Pane_password, text='新密码：', font=("微软雅黑", 14))
    Label_pwd.place(x=65, y=100)
    var_pwd = StringVar()
    Entry_pwd = Entry(Pane_password, textvariable=var_pwd, font=("微软雅黑", 14), width=16)
    Entry_pwd.place(x=140, y=102)
    # 再次确认密码
    Label_pwd_again = Label(Pane_password, text='确认密码：', font=("微软雅黑", 14))
    Label_pwd_again.place(x=50, y=160)
    var_pwd_again = StringVar()
    Entry_pwd_again = Entry(Pane_password, textvariable=var_pwd_again, font=("微软雅黑", 14), width=16)
    Entry_pwd_again.place(x=140, y=162)
    # 按钮
    Button(Pane_password, text='确定', font=('华文行楷', 15), command=save_change_password).place(x=120, y=230)
    Button(Pane_password, text='返回', font=('华文行楷', 15), command=close_change_password_window).place(x=230, y=230)


def remove_user():  # 删除账号函数
    a = var_Combobox.get()
    try:
        cursor.execute('delete from 管理员 where 账号=%s', a)
        connection.commit()
    except pymysql.DatabaseError:
        connection.rollback()
    else:
        messagebox.showinfo(title='提示', message='删除成功')
        delete_users_root.destroy()


def close_delete_users():  # 关闭删除账号窗口
    delete_users_root.destroy()


def delete_users():  # 删除账号窗口
    global delete_users_root, var_Combobox
    delete_users_root = Toplevel(user_root)
    delete_users_root.title('删除账号')
    delete_users_root.geometry('300x200')
    delete_users_root.iconbitmap('图标.ico')
    delete_users_root.resizable(0, 0)
    delete_users_root['bg'] = 'DeepSkyBlue'
    user_ls = []
    cursor.execute('select 账号 from 管理员')
    ls = cursor.fetchall()
    for i in ls:
        user_ls.append(i)
    Pand_users = PanedWindow(delete_users_root, width=290, height=190)
    Pand_users.place(x=5, y=5)
    Label_delete_users = Label(Pand_users, text='账号：', font=("微软雅黑", 14))
    Label_delete_users.place(x=20, y=50)
    var_Combobox = StringVar()
    Combobox_Entry = Combobox(Pand_users, textvariable=var_Combobox, font=("微软雅黑", 14), width=12)
    Combobox_Entry['value'] = ls
    Combobox_Entry.place(x=80, y=50)
    Button(Pand_users, text='删除', font=('华文行楷', 14), command=remove_user).place(x=70, y=120)
    Button(Pand_users, text='返回', font=('华文行楷', 14), command=close_delete_users).place(x=160, y=120)


def new_window():  # 主窗口
    global Tree, Search_room, Search_name, Search_ID, user_root, user_photo
    root_new.destroy()
    user_root = Tk()
    user_root.title('欢迎使用')
    user_root.iconbitmap('图标.ico')
    user_root.resizable(0, 0)
    user_root.geometry("900x640+180+80")
    user_root['bg'] = 'DeepSkyBlue'
    user_photo = PhotoImage(file="欢迎使用.png")
    usert_image_lable = Label(user_root, image=user_photo)
    usert_image_lable.pack()
    # 左侧按钮区域
    bt_left = PanedWindow(user_root, width=200, height=535)
    bt_left.place(x=4, y=94)
    # 添加按钮
    Button_add = Button(bt_left, text="添加客户", font=('华文行楷', 16), command=add_window)
    Button_add.place(x=50, y=20)
    Button_update = Button(bt_left, text="修改客户", font=('华文行楷', 16), command=alter_window)
    Button_update.place(x=50, y=70)
    Button_delete = Button(bt_left, text="删除客户", font=('华文行楷', 16), command=delete_window)
    Button_delete.place(x=50, y=120)
    Button_room = Button(bt_left, text="管理客房", font=('华文行楷', 16), command=room_window)
    Button_room.place(x=50, y=170)
    Button_modify = Button(bt_left, text="更改密码", font=('华文行楷', 16), command=change_password_window)
    Button_modify.place(x=50, y=220)
    Button_remove = Button(bt_left, text="删除账号", font=('华文行楷', 16), command=delete_users)
    Button_remove.place(x=50, y=270)
    # 右侧按钮区域
    bt_right = PanedWindow(user_root, width=685, height=535)
    bt_right.place(x=210, y=94)

    LabelFrame_query = LabelFrame(bt_right, text="客户信息查询", width=674, height=70)
    LabelFrame_query.place(x=6, y=10)
    # 添加控件 房号
    Label_room = Label(bt_right, text="房号：")
    Label_room.place(x=25, y=35)
    Search_room = StringVar()
    Entry_room = Entry(bt_right, textvariable=Search_room, width=10)
    Entry_room.place(x=85, y=35)
    # 姓名
    Label_name = Label(bt_right, text="姓名：")
    Label_name.place(x=160, y=35)
    Search_name = StringVar()
    Entry_name = Entry(bt_right, textvariable=Search_name, width=10)
    Entry_name.place(x=205, y=35)
    # 身份证号
    Label_ID = Label(bt_right, text="身份证号：")
    Label_ID.place(x=285, y=35)
    Search_ID = StringVar()
    Entry_ID = Entry(bt_right, textvariable=Search_ID, width=15)
    Entry_ID.place(x=345, y=35)
    # 按钮
    Button_query = Button(bt_right, text="查询", font=('华文行楷', 12), command=search)
    Button_query.place(x=500, y=35)
    Button_all = Button(bt_right, text="显示全部", font=('华文行楷', 12), command=search_all)
    Button_all.place(x=580, y=35)
    # 添加TreeView控件
    Tree = Treeview(bt_right, columns=("room_id", "name", "sex", "ID",
                                       "in_time", "out_time", "room_type"), show="headings", height=21)
    Tree.bind("<Double-Button-1>", view_data)  # 左键双击事件
    # 设置每一个列的宽度和对齐的方式
    Tree.column("room_id", width=80, anchor="center")
    Tree.column("name", width=80, anchor="center")
    Tree.column("sex", width=70, anchor="center")
    Tree.column("ID", width=120, anchor="center")
    Tree.column("in_time", width=120, anchor="center")
    Tree.column("out_time", width=120, anchor="center")
    Tree.column("room_type", width=80, anchor="center")
    # 设置每个列的标题
    Tree.heading("room_id", text="房间")
    Tree.heading("name", text="姓名")
    Tree.heading("sex", text="性别")
    Tree.heading("ID", text="身份证号")
    Tree.heading("in_time", text="入住时间")
    Tree.heading("out_time", text="退房时间")
    Tree.heading("room_type", text="房间类型")
    # 添加
    Tree.place(x=6, y=80)
    # 添加实时用户与登录时间
    Label_login_user = Label(user_root, text="当前用户：" + username.get() +
                                             "\t\t\n   登录时间：" + login_time, bg='white')
    Label_login_user.place(x=650, y=40)


def new():  # 666窗口
    global root_new, photo_new
    root_new = Tk()  # 第一个框架用于放输入组件和对应的提示标签
    root_new.title("666")
    root_new.iconbitmap('图标.ico')
    root_new.resizable(0, 0)
    root_new.geometry("620x420+400+100")
    root_new["bg"] = "white"
    photo_new = PhotoImage(file="666.png")
    photo_new_lable = Label(root_new, text='\t\t\t\t#include<stdio.h>\n\t\t\t\tint main()\n\t\t\t\t{\n\t\t\t\tint '
                                           'a=6;\n\t\t\t\tfor(int i=0;i<3;i++){ '
                                           '\n\t\t\t\tprintf("%d",a);\n\t\t\t\t}\n\t\t\t\t\treturn 0;\n\t\t\t\t}',
                            font=16, justify=LEFT, image=photo_new, compound=CENTER)
    photo_new_lable.pack(padx=10, pady=10)
    bt3 = Button(root_new, text='登录成功欢迎使用点击进入', font=('华文行楷', 20), command=new_window, fg='DeepSkyBlue')
    bt3.pack(padx=10, pady=10)


def save_sign():  # 注册函数
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


def close_sign():  # 关闭注册界面
    sign_root.destroy()


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
    Button(Pane_sign, text='确定', font=('华文行楷', 15), command=save_sign).place(x=120, y=210)
    Button(Pane_sign, text='返回', font=('华文行楷', 15), command=close_sign).place(x=230, y=210)


def login(event):  # 登录函数
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
            new()
        else:
            messagebox.showwarning(title='提示', message='密码错误')
    else:
        messagebox.showwarning(title='提示', message='账号错误')
