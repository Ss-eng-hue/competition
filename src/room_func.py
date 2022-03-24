from tkinter import messagebox
from tkinter import *
import pymysql
from my_sql import cursor
from my_sql import connection


def show_room(room_Tree):  # 显示房间信息
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


def save_room_data(room_Tree):  # 保存房间数据
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
    show_room(room_Tree)


def alter_room_data(room_Tree):  # 修改房间数据
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
    show_room(room_Tree)


def remove_room_data(room_Tree):  # 删除房间
    a = room_id.get()
    try:
        cursor.execute('delete from 客房 where 房号=%s', a)
        connection.commit()
    except pymysql.DatabaseError:
        connection.rollback()
    else:
        messagebox.showinfo(title='提示', message='删除成功')
        add_alter_root.destroy()
    show_room(room_Tree)


def close_add_alter_room_window():  # 关闭房间明细窗口
    add_alter_root.destroy()


def add_alter_room_window(sign, room_root):  # 管理房间窗口
    global add_alter_root, room_id, room_mold, room_cost
    add_alter_root = Toplevel(room_root)
    if sign == '1':
        add_alter_root.title("添加客房")
    elif sign == '2':
        add_alter_root.title("修改客房")
    elif sign == '3':
        add_alter_root.title("删除客房")
    add_alter_root.geometry("400x300+900+100")
    add_alter_root.iconbitmap('../pic/图标.ico')
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


def add_room(room_Tree):  # 添加房间
    add_alter_room_window('1', room_Tree)


def alter_room(room_Tree):  # 修改房间
    item = room_Tree.selection()[0]
    add_alter_room_window('2', room_Tree)
    info_list = room_Tree.item(item, "values")
    room_id.set(info_list[0])
    room_mold.set(info_list[1])
    room_cost.set(info_list[2])


def remove_room(room_Tree):  # 删除房间
    item = room_Tree.selection()[0]
    add_alter_room_window('3', room_Tree)
    info_list = room_Tree.item(item, "values")
    room_id.set(info_list[0])
    room_mold.set(info_list[1])
    room_cost.set(info_list[2])


def close_room_window(room_root):  # 关闭管理房间窗口
    room_root.destroy()
