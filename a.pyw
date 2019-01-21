from tkinter import *
from tkinter import messagebox
import r

input_items = '字段名', '训练次数'
input_list = []


def create_form(base_window, d_start, d_word, d_signal):
    global input_list
    area = Frame(base_window)
    btn = Button(area, text='选择字段', command=(lambda: create_multi_select(base_window)))
    area.pack(side=TOP, fill=X, padx=5, pady=5)
    btn.pack(side=LEFT)

    area = Frame(base_window)
    lab = Label(area, width=15, text='1.平假名 2.片假名')
    ent = Entry(area)
    area.pack(side=TOP, fill=X, padx=5, pady=5)
    lab.pack(side=LEFT)
    ent.pack(side=RIGHT, expand=YES, fill=X)
    input_list.append({'type': ent})

    area = Frame(base_window)
    btn_start = Button(area, text='Start', command=d_start)
    btn_word = Button(area, text='Word', command=d_word)
    btn_answer = Button(area, text='Answer', command=d_signal)
    area.pack(side=TOP, fill=X, padx=5, pady=5)
    btn_start.pack(side=LEFT, padx=5, pady=5)
    btn_answer.pack(side=RIGHT, padx=5, pady=5)
    btn_word.pack(side=RIGHT, padx=5, pady=5)

    area = Frame(base_window)
    lab_word = Label(area, width=10, textvariable=g_word)
    lab_signal = Label(area, width=20, textvariable=g_signal, background='white')
    area.pack(side=TOP, fill=X, padx=5, pady=5)
    lab_word.pack(side=LEFT)
    lab_signal.pack(side=RIGHT)

    area = Frame(base_window)
    btn_quit = Button(area, width=20, text='Quit', command=base_window.quit)
    area.pack(side=TOP, padx=5, pady=5)
    btn_quit.pack(side=TOP, padx=5, pady=5)


has_selected_list = []


def default_select_list(list_len):
    global has_selected_list
    for i in range(list_len):
        has_selected_list.append(0)


def change_selected_state(index):
    global has_selected_list
    if has_selected_list[index] == 0:
        has_selected_list[index] = 1
    else:
        has_selected_list[index] = 0


def create_multi_select(base_window):
    cbtn_a = Checkbutton(base_window, width=15, text='A行', command=lambda: change_selected_state(0))
    cbtn_k = Checkbutton(base_window, width=15, text='K行', command=lambda: change_selected_state(1))
    cbtn_s = Checkbutton(base_window, width=15, text='S行', command=lambda: change_selected_state(2))
    cbtn_t = Checkbutton(base_window, width=15, text='T行', command=lambda: change_selected_state(3))
    cbtn_n = Checkbutton(base_window, width=15, text='N行', command=lambda: change_selected_state(4))
    cbtn_h = Checkbutton(base_window, width=15, text='H行', command=lambda: change_selected_state(5))
    cbtn_m = Checkbutton(base_window, width=15, text='M行', command=lambda: change_selected_state(6))
    cbtn_y = Checkbutton(base_window, width=15, text='Y行', command=lambda: change_selected_state(7))
    cbtn_r = Checkbutton(base_window, width=15, text='R行', command=lambda: change_selected_state(8))
    cbtn_w = Checkbutton(base_window, width=15, text='W行', command=lambda: change_selected_state(9))
    cbtn_n2 = Checkbutton(base_window, width=15, text='N2行', command=lambda: change_selected_state(10))
    cbtn_g = Checkbutton(base_window, width=15, text='G行', command=lambda: change_selected_state(11))
    cbtn_z = Checkbutton(base_window, width=15, text='Z行', command=lambda: change_selected_state(12))
    cbtn_d = Checkbutton(base_window, width=15, text='D行', command=lambda: change_selected_state(13))
    cbtn_b = Checkbutton(base_window, width=15, text='B行', command=lambda: change_selected_state(14))
    cbtn_p = Checkbutton(base_window, width=15, text='P行', command=lambda: change_selected_state(15))
    cbtn_xxx = Checkbutton(base_window, width=15, text='XXX行', command=lambda: change_selected_state(16))
    cbtn_a.pack(anchor=CENTER)
    cbtn_k.pack(anchor=CENTER)
    cbtn_s.pack(anchor=CENTER)
    cbtn_t.pack(anchor=CENTER)
    cbtn_n.pack(anchor=CENTER)
    cbtn_h.pack(anchor=CENTER)
    cbtn_m.pack(anchor=CENTER)
    cbtn_y.pack(anchor=CENTER)
    cbtn_r.pack(anchor=CENTER)
    cbtn_w.pack(anchor=CENTER)
    cbtn_n2.pack(anchor=CENTER)
    cbtn_g.pack(anchor=CENTER)
    cbtn_z.pack(anchor=CENTER)
    cbtn_d.pack(anchor=CENTER)
    cbtn_b.pack(anchor=CENTER)
    cbtn_p.pack(anchor=CENTER)
    cbtn_xxx.pack(anchor=CENTER)


def get_selected_row(list_row):
    i = 0
    selected_row = []
    for tmp in list_row:
        if tmp == 1:
            selected_row.append(r.whole_word[i])
        i += 1
    return selected_row


def get_data():
    return r.random_select(get_selected_row(has_selected_list))


def init_w_s():
    global g_word, g_signal
    g_word = StringVar()
    g_signal = StringVar()
    g_word.set('未定义')
    g_signal.set('未定义')


def default_w_s(m_hint):
    global g_word, g_signal
    g_word.set(m_hint)
    g_signal.set(m_hint)


w_s = ()
g_word = None
g_signal = None
is_success_start = False


def start_all():
    global w_s, is_success_start
    is_success_start = False
    type_num = (input_list[0]['type']).get()
    if type_num != '1' and type_num != '2':
        messagebox.showinfo(title='input error', message='请输入正确的假名类型')
        default_w_s('未定义')
    else:
        selected_row = get_selected_row(has_selected_list)
        if len(selected_row) != 0:
            w_s = r.random_select(selected_row, type_num)
            is_success_start = True
            default_w_s('已定义')
        else:
            default_w_s('未定义')


def display_word():
    global g_word
    if is_success_start:
        g_word.set(w_s[0])


def display_signal():
    global g_signal
    if is_success_start:
        g_signal.set(w_s[1])


if __name__ == '__main__':
    t = Tk()
    init_w_s()
    if len(has_selected_list) == 0:
        default_select_list(len(r.whole_word))
    create_form(t, start_all, display_word, display_signal)
    t.mainloop()
