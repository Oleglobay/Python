from tkinter import*
from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def helloCallBack():
    msg = messagebox.showinfo("hello python","hello world")

B = Button(top, text = "hello", command = helloCallBack)
B.place(x = 50,y = 50)
top.mainloop()
