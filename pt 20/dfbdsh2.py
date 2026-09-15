from tkinter import*

def b1(event):
    root.title("Left button mouse")

def b3(event):
    root.title("Right button mouse")

def move(event):
    x = event.x
    y = event.y
    s = "mouse movement {}x{}".format(x, y)
    root.title(s)

root = Tk()
root.minsize(width=500, height=400)

root.bind('<Button-1>', b1)
root.bind('<Button-3>', b3)
root.bind('<Motion>', move)

root.mainloop()
