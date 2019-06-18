from tkinter import (Tk,
                     Label, Entry, Button, Listbox, Scrollbar, Frame, 
                     StringVar, END)
from CaptionAssisant import new_idiom


def run():
    '''
    获取e_theme_word中输入的主题词，调用get_df函数得到谐音替换后的成语，最后输出到
    lb_tuple这个ListBox中
    '''
    word = e_theme_word.get()
    df = new_idiom(word)
    lb_tuple.set(tuple(df['new_idiom']))


root = Tk()
root.title('标题助手')
root.geometry('250x300')

frame = Frame(root)
# 运行按钮
b_run = Button(frame, width=10, text='搜 索', fg='red', command=run)
b_run.grid(row=0, column=1, columnspan=3, pady=10)

# 主题词标签
l_theme_word = Label(frame, text='主题词')
l_theme_word.grid(row=1, pady=5)
# 主题词输入框
e_str = StringVar()
e_theme_word = Entry(frame, textvariable=e_str)
e_theme_word.grid(row=1, column=1, pady=5)
#e_str.set('在这里输入主题词')

# 参考标题标签
l_title_ref = Label(frame, text='参考标题')
l_title_ref.grid(row=2)
# 参考标题列表框
lb_tuple = StringVar()
lb_title_ref = Listbox(frame, listvariable=lb_tuple)
lb_title_ref.grid(row=2, column=1)
# 给参考标题列表框添加滚动条
sl_lb = Scrollbar(frame, command=lb_title_ref.yview)
sl_lb.grid(row=2, column=2, sticky='ns') # sticky='ns'表示垂直拉伸
# 设置参考标题列表框的回调函数，使列表框和滚动条保持同步
lb_title_ref.config(yscrollcommand=sl_lb.set)

frame.pack(side='left')
root.mainloop()