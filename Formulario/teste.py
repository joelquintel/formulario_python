from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('600x600')

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

txt = Entry(window,width=10)

txt.grid(column=1, row=0)

lbl2 = Label(window, text="Hello")

lbl2.grid(column=5, row=0)

txt2 = Entry(window,width=10)

txt2.grid(column=7, row=0)


def clicked():

    res = "Welcome to " + txt.get()

    lbl.configure(text= res)

btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=2, row=15)

window.mainloop()