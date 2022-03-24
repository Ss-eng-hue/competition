from login import *
from window import *


def new_window(username, login_time):  # 主窗口
    global Tree, Search_room, Search_name, Search_ID, user_root, user_photo
    root_new.destroy()
    user_root = Tk()
    user_root.title('欢迎使用')
    user_root.iconbitmap('../pic/图标.ico')
    user_root.resizable(0, 0)
    user_root.geometry("900x640+180+80")
    user_root['bg'] = 'DeepSkyBlue'
    user_photo = PhotoImage(file="../pic/欢迎使用.png")
    usert_image_lable = Label(user_root, image=user_photo)
    usert_image_lable.pack()
    # 左侧按钮区域
    bt_left = PanedWindow(user_root, width=200, height=535)
    bt_left.place(x=4, y=94)
    # 添加按钮
    Button_add = Button(bt_left, text="添加客户", font=('华文行楷', 16), command=lambda: show_window('1', user_root, Tree))
    Button_add.place(x=50, y=20)
    Button_update = Button(bt_left, text="修改客户", font=('华文行楷', 16), command=lambda: alter_window(Tree, user_root))
    Button_update.place(x=50, y=70)
    Button_delete = Button(bt_left, text="删除客户", font=('华文行楷', 16), command=lambda: delete_window(Tree, user_root))
    Button_delete.place(x=50, y=120)
    Button_room = Button(bt_left, text="管理客房", font=('华文行楷', 16), command=lambda: room_window(user_root))
    Button_room.place(x=50, y=170)
    Button_modify = Button(bt_left, text="更改密码", font=('华文行楷', 16),
                           command=lambda: change_password_window(user_root, username))
    Button_modify.place(x=50, y=220)
    Button_remove = Button(bt_left, text="删除账号", font=('华文行楷', 16), command=lambda: delete_users(user_root))
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
    Button_query = Button(bt_right, text="查询", font=('华文行楷', 12),
                          command=lambda: search(Tree, Search_room, Search_name, Search_ID))
    Button_query.place(x=500, y=35)
    Button_all = Button(bt_right, text="显示全部", font=('华文行楷', 12), command=lambda: search_all(Tree))
    Button_all.place(x=580, y=35)
    # 添加TreeView控件
    Tree = Treeview(bt_right, columns=("room_id", "name", "sex", "ID",
                                       "in_time", "out_time", "room_type"), show="headings", height=21)
    #  事件处理带参
    Tree.bind("<Double-Button-1>", lambda event: view_data(event, user_root, Tree))  # 左键双击事件
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


def new(user, login_t):  # 666窗口
    global root_new, photo_new
    root_new = Tk()  # 第一个框架用于放输入组件和对应的提示标签
    root_new.title("666")
    root_new.iconbitmap('../pic/图标.ico')
    root_new.resizable(0, 0)
    root_new.geometry("620x420+400+100")
    root_new["bg"] = "white"
    photo_new = PhotoImage(file="../pic/666.png")
    photo_new_lable = Label(root_new, text='\t\t\t\t#include<stdio.h>\n\t\t\t\tint main()\n\t\t\t\t{\n\t\t\t\tint '
                                           'a=6;\n\t\t\t\tfor(int i=0;i<3;i++){ '
                                           '\n\t\t\t\tprintf("%d",a);\n\t\t\t\t}\n\t\t\t\t\treturn 0;\n\t\t\t\t}',
                            font=16, justify=LEFT, image=photo_new, compound=CENTER)
    photo_new_lable.pack(padx=10, pady=10)
    bt3 = Button(root_new, text='登录成功欢迎使用点击进入', font=('华文行楷', 20), command=lambda: new_window(user, login_t),
                 fg='DeepSkyBlue')
    bt3.pack(padx=10, pady=10)
