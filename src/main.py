from login import *

root = Tk()  # 创建Tk控件
root.title("登录界面")  # 窗口标题
root.iconbitmap('../pic/图标.ico')  # 窗口图标
root.geometry("620x420+400+150")  # 窗口大小
root.resizable(0, 0)  # 窗体大小不允许变，两个参数分别代表x轴和y轴
root["bg"] = "DeepSkyBlue"  # 背景颜色
# 创建一个Label标签展示图片并设为背景
# 背景图片
photo = PhotoImage(file="../pic/登录.png")
image_lable = Label(
    root, image=photo, text='\t\t大数据与人工智能学院\n\n\t\t\t民宿管理系统',
    justify=LEFT, compound=CENTER, font=('华文行楷', 26))
image_lable.pack(padx=10, pady=10)

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
login_bt = Button(root, text="登录", width=4, font=('华文行楷', 16), command=lambda: log_in(username, password, root))
login_bt.pack(side=RIGHT, padx=20, pady=10)
clear_bt = Button(root, text='注册', width=4, font=('华文行楷', 16), command=lambda: sign_window(root))
clear_bt.pack(side=RIGHT, padx=20, pady=10)

mainloop()
