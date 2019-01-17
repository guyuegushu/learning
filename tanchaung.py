import tkinter as tk
from tkinter import messagebox        #引入弹窗库
window=tk.Tk()
window.title('my window')
window.geometry('500x600')
 
def hit_me():
    #tc1=messagebox.askokcancel(title='hello',message='hello word') #弹窗 return True/False
    #print (tc1)
    #tc2=messagebox.askquestion(title='hello',message='hello word') #return yes/no
    #print (tc2)
    tc3=messagebox.showinfo(title='hello',message='hello word')  # return ok
    print (tc3)
tk.Button(window,text='hit me',command=hit_me).pack()
 
window.mainloop()
