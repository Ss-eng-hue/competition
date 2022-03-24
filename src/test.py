from tkinter import *


def handler_button():
    paramStr.set('button：no param ')


def param_button(param):
    paramStr.set(f'button：{param}')


# 事件处理函数
def handler(event):
    paramStr.set('event：no param ')


# 事件处理函数带参数
def handler_args(event, param):
    paramStr.set(f'event：{param}')


# 中介函数
def handler_adaptor(fun, **kwds):
    return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)


if __name__ == '__main__':
    root = Tk()
    paramStr = StringVar()
    paramStr.set('button：')
    Label(root, textvariable=paramStr).pack()
    btn1 = Button(root, text='无参按钮', command=handler_button)  # 默认左键点击
    btn2 = Button(root, text='带参按钮1', command=lambda: param_button("param"))
    btn1.bind('<Button-3>', handler)  # 右键点击
    # 带参绑定方法1，使用lambda 
    btn1.bind('<Double-Button-1>', lambda event: handler_args(event, "double left"))  # 左键双击
    # 带参绑定方法2，使用中间函数，但要注意指定参数名
    btn1.bind('<Double-Button-3>', handler_adaptor(handler_args, param="double right"))  # 右键双击

    btn1.pack()
    btn2.pack()
    root.mainloop()
