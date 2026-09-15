from tkinter import *

def about():
    a = Toplevel()
    a.geometry('200x150')
    a['bg'] = 'white'
    a.overrideredirecrt(True)
    Label(a, text="ggggg").pack(expand=1)
    a.after(5000, lambda: a.destroy())

root = Tk()
Button(text="no", width=20).pack()
Label(text="label", width=20, height=3).pack()
Button(text="start", width=20, command=about).pack()

root.mainloop()
