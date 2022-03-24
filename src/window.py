from tkinter.ttk import Combobox, Treeview
from func import *
from room_func import *


def alter_window(Tree, user_root):  # 修改窗口
    ls = []
    item = Tree.selection()[0]
    show_window('2', user_root, Tree)
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


def delete_window(Tree, user_root):  # 删除窗口
    global delete_root, delete_photo, delete_room, delete_name, delete_ID
    delete_root = Toplevel(user_root)
    delete_root.title('删除信息')
    delete_root.iconbitmap('../pic/图标.ico')
    delete_root.geometry("600x400+600+150")
    delete_root.resizable(0, 0)  # 不能改变大小
    delete_root['bg'] = 'DeepSkyBlue'
    # 添加图片
    delete_photo = PhotoImage(file="../pic/明细窗口.png")
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
    Button(delete_root, text="删除", font=('华文行楷', 15),
           command=lambda: delete_data(Tree, delete_room, delete_name, delete_ID, delete_root)).place(x=235, y=300)
    Button(delete_root, text="关闭", font=('华文行楷', 15), command=lambda: delete_close(delete_root)).place(x=335, y=300)


def show_window(sign, user_root, Tree):  # 明细窗口
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
    data_root.iconbitmap('../pic/图标.ico')
    data_root.resizable(0, 0)  # 不能改变大小
    data_root['bg'] = 'DeepSkyBlue'
    # 添加图片
    data_photo = PhotoImage(file="../pic/明细窗口.png")
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
        Button_save_change = Button(data_root, text="保存", font=('华文行楷', 15),
                                    command=lambda: save_data(Tree, var_room, var_name, var_ID, var_sex, var_nb,
                                                              var_in_time, var_out_time, var_room_typle, var_days,
                                                              var_cost, var_native, data_root))
        Button_save_change.place(x=400, y=420)
    elif sign == '2':
        Button_save_change = Button(data_root, text="修改", font=('华文行楷', 15),
                                    command=lambda: change_data(Tree, var_room, var_ID, var_nb, var_in_time,
                                                                var_out_time, var_room_typle, var_days, var_cost,
                                                                data_root))
        Button_save_change.place(x=400, y=420)
    Button(data_root, text="关闭", font=('华文行楷', 15), command=lambda: show_close(data_root)).place(x=502, y=420)
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


def room_window(user_root):  # 管理窗口
    global room_root, room_Tree
    room_root = Toplevel(user_root)
    room_root.title("管理客房")
    room_root.iconbitmap('../pic/图标.ico')
    room_root.resizable(0, 0)
    room_root.geometry("600x400+800+200")
    room_root['bg'] = 'DeepSkyBlue'
    # 左侧按钮块
    Pane_room_left = PanedWindow(room_root, width=190, height=380)
    Pane_room_left.place(x=5, y=8)
    Button(Pane_room_left, text="显示全部", font=('华文行楷', 15), command=lambda: show_room(room_Tree)).place(x=50, y=20)
    Button(Pane_room_left, text="添加客房", font=('华文行楷', 15), command=lambda: add_room(room_Tree)).place(x=50, y=70)
    Button(Pane_room_left, text="修改客房", font=('华文行楷', 15), command=lambda: alter_room(room_Tree)).place(x=50, y=120)
    Button(Pane_room_left, text="删除客房", font=('华文行楷', 15), command=lambda: remove_room(room_Tree)).place(x=50, y=170)
    Button(Pane_room_left, text="关        闭", font=('华文行楷', 15), command=lambda: close_room_window(room_root)).place(
        x=50, y=220)
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


def view_data(event, user_root, Tree):  # 双击窗口
    ls = []
    item = Tree.selection()[0]
    show_window('3', user_root, Tree)
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


def change_password_window(user_root, username):  # 修改密码窗口
    global password_root, var_zh, var_pwd, var_pwd_again
    password_root = Toplevel(user_root)
    password_root.title("修改密码")
    password_root.iconbitmap('../pic/图标.ico')
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
    Button(Pane_password, text='确定', font=('华文行楷', 15),
           command=lambda: save_change_password(password_root, var_zh, var_pwd, var_pwd_again)).place(x=120, y=230)
    Button(Pane_password, text='返回', font=('华文行楷', 15),
           command=lambda: close_change_password_window(password_root)).place(x=230, y=230)


def delete_users(user_root):  # 删除账号窗口
    global delete_users_root, var_Combobox
    delete_users_root = Toplevel(user_root)
    delete_users_root.title('删除账号')
    delete_users_root.geometry('300x200')
    delete_users_root.iconbitmap('../pic/图标.ico')
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
    Button(Pand_users, text='删除', font=('华文行楷', 14),
           command=lambda: remove_user(var_Combobox, delete_users_root)).place(x=70, y=120)
    Button(Pand_users, text='返回', font=('华文行楷', 14), command=lambda: close_delete_users(delete_users_root)).place(x=160,
                                                                                                                  y=120)
