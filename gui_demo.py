from tkinter import *


def myEvent1():
    if c1.get() == 1:
        s1["text"]="语文被选中"
    else:
        
        s1["text"]="语文被取消"

def myEvent2():
    if c2.get() == 1:
        s2["text"]="数学被选中"
    else:
        s2["text"]="数学被取消"

top=Tk()
c1=StringVar() # 必须在创建根窗口之后定义，可以使用get()函数获取值
c2=StringVar()
top.wm_title("复选框")
top.geometry("400x300+300+200")

cc1=Checkbutton(top,text="语文", variable=c1, onvalue = '语文被选中', offvalue = '语文被取消')
cc1.pack()
cc2=Checkbutton(top,text="数学", variable=c2, onvalue = '数学被选中', offvalue = '数学被取消')
cc2.pack()

s1=Label(top,textvariable=c1)
s1.pack()
s2=Label(top,textvariable=c2)
s2.pack()

top.mainloop()
