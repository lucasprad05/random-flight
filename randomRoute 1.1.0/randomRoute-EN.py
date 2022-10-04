#Random Flight Route Ideas
#by Lucas Prado
#Co-created by Joao Paulo

import random
from tkinter import *

class MyWindow:
    
    def __init__(self, win):
        self.my_list = []

        self.lbl1 = Label(win, text='Airport ICAO')
        self.lbl1.place(x = 70, y = 40)
        self.t1 = Entry()
        self.t1.place(x = 150, y = 41)

        self.lbl2 = Label(win, text='Route')
        self.lbl2.place(x = 80, y = 131)
        self.t2 = Entry()
        self.t2.place(x = 150, y = 131)

        self.btn1 = Button(win, text='Add')
        self.b1 = Button(win, text='Add', command = self.add)
        self.b1.place(x = 85, y = 82)

        self.btn2 = Button(win, text='Sort')
        self.b2 = Button(win, text='Sort', command = self.sort)
        self.b2.place(x = 150, y = 82)

        self.lbl3 = Label(win, text='Developed by Lucas Prado')
        self.lbl3.place (x = 198, y = 198)

    def add(self):
        apt = self.t1.get()
        self.my_list.append(apt)
        self.t1.delete(0, 'end')

    def sort(self):
        self.t2.delete(0, 'end')
        N = len(self.my_list) - 1
        apt1 = random.randint(0, N)
        apt2 = random.randint(0, N)
        if self.my_list[apt1] == self.my_list[apt2]:
            return self.sort()
        self.t2.insert(END, f"{self.my_list[apt1]}  -  {self.my_list[apt2]}")


window = Tk()
mywin = MyWindow(window)
window.title('Random Route')
window.iconbitmap('iconPlane.ico')
window.geometry("350x220")
window.resizable(width = False, height = False)
window.mainloop()