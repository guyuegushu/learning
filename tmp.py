from tkinter import *


def main():
    root = Tk()
    menubar = Menu(root)
    open_var = IntVar()
    save_var = IntVar()
    quit_var = IntVar()

    file_menu = Menu(menubar, tearoff=False)
    menubar.add_cascade(label='菜部', menu=file_menu)
    file_menu.add_checkbutton(label='大蒜', variable=open_var)
    file_menu.add_checkbutton(label='油菜', variable=save_var)
    file_menu.add_checkbutton(label='香菜', variable=quit_var)
    root.config(menu=menubar)
    mainloop()

if __name__ == '__main__':
    main()
