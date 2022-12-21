from tkinter import *
from time import sleep

win = Tk()
win.geometry('1000x300')
win.title('ГУЛИ ААААААААААА')
win.resizable(False, False)

def gul():
    gul_num = 1000

    while gul_num > 6:

        gul_num -= 7

        if gul_num <= 6:
            gul_num = 'А вот все'
            text.configure(text=str(gul_num))
            break

        text.configure(text=str(gul_num)+'-7')

        win.update()
        sleep(0.05)

text = Label(win, text='1000-7', font='Calibri 80')
btn = Button(win, text='ЗАПУСТИТЬ ГУЛЕЙ', font='Calibri 50', command=gul)

text.pack()
btn.pack()

win.mainloop()