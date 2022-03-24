from tkinter import messagebox
import pymysql
from my_sql import cursor
from my_sql import connection


def search_all(Tree):  # 显示全部
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


def search(Tree, Search_room, Search_name, Search_ID):  # 查询函数
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


def delete_data(Tree, delete_room, delete_name, delete_ID, delete_root):  # 删除函数
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
    search_all(Tree)


def delete_close(delete_root):  # 关闭删除窗口
    delete_root.destroy()


def save_data(Tree, var_room, var_name, var_ID, var_sex, var_nb, var_in_time, var_out_time, var_room_typle, var_days,
              var_cost, var_native, data_root):  # 添加函数
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
    search_all(Tree)


def change_data(Tree, var_room, var_ID, var_nb, var_in_time, var_out_time, var_room_typle, var_days, var_cost,
                data_root):  # 修改函数
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
    search_all(Tree)


def show_close(data_root):  # 关闭明细窗口
    data_root.destroy()


def save_change_password(password_root, var_zh, var_pwd, var_pwd_again):  # 修改密码函数
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


def close_change_password_window(password_root):  # 关闭修改密码窗口
    password_root.destroy()


def remove_user(var_Combobox, delete_users_root):  # 删除账号函数
    a = var_Combobox.get()
    try:
        cursor.execute('delete from 管理员 where 账号=%s', a)
        connection.commit()
    except pymysql.DatabaseError:
        connection.rollback()
    else:
        messagebox.showinfo(title='提示', message='删除成功')
        delete_users_root.destroy()


def close_delete_users(delete_users_root):  # 关闭删除账号窗口
    delete_users_root.destroy()
