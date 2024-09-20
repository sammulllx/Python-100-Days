"""
使用tkinter创建GUI
- 顶层窗口
- 控件
- 布局
- 事件回调

Version: 0.1
Author: 骆昊
Date: 2018-03-14
"""

# 引入 tkinter 模块，用于创建 GUI 界面
import tkinter
# 引入 tkinter 的 messagebox 模块，用于弹出消息对话框
import tkinter.messagebox


def main():
    # 定义一个布尔变量，控制标签文本的切换
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag  # 使用 nonlocal 关键字以修改外部作用域的变量
        # 切换 flag 值
        flag = not flag
        # 根据 flag 值设置文本内容和颜色
        color, msg = ('red', 'Hello, world sam!')\
            if flag else ('blue', 'Goodbye, world!')
        # 使用 config 方法修改 label 的文本和颜色属性
        label.config(text=msg, fg=color)

    # 弹出确认对话框，确认是否退出
    def confirm_to_quit():
        # 使用 messagebox 弹出对话框，返回布尔值表示是否确认
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            # 如果用户选择确定，关闭主窗口
            top.quit()

    # 创建顶层窗口对象（主窗口）
    top = tkinter.Tk()
    # 设置窗口的尺寸为 240x160 像素
    top.geometry('240x160')
    # 设置窗口的标题
    top.title('小游戏')

    # 创建一个标签对象，设置初始文字、字体、字体颜色等属性
    label = tkinter.Label(top, text='Hello, world sams!',
                          font='Arial -32', fg='red')
    # 使用 pack 方法自动布局标签，expand=1 表示标签将尽量扩展以填充窗口空间
    label.pack(expand=1)

    # 创建一个 Frame 框架（容器）用于放置按钮
    panel = tkinter.Frame(top)

    # 创建第一个按钮，文本为“修改”，点击时调用 change_label_text 函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    # 使用 pack 方法布局按钮，side='left' 表示放置在容器的左边
    button1.pack(side='left')

    # 创建第二个按钮，文本为“退出”，点击时调用 confirm_to_quit 函数
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    # 使用 pack 方法布局按钮，side='right' 表示放置在容器的右边
    button2.pack(side='right')

    # 将按钮容器放置在主窗口的底部（side='bottom'）
    panel.pack(side='bottom')

    # 启动主事件循环，窗口保持运行，等待用户交互
    tkinter.mainloop()


# 如果该文件作为主程序运行，调用 main 函数启动 GUI 应用程序
if __name__ == '__main__':
    main()
