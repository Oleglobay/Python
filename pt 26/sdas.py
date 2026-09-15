from tkinter import *

def circle():
    c.create_oval(
        x,y, x + 30, y + 30)

def circle1():
    c.create_rectangle(
        x,y, x + 30, y + 30)
    
def circle2():
    c.create_polygon(
        x,y,x + 25,y + 30,x - 25,y + 30)
    
def popup(event):
    global x, y
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)

root = Tk()
c = Canvas(width=300, height=300, bg='white')
c.pack()
c.bind("<Button-3>", popup)
menu = Menu(tearoff=0)
    
menu.add_command(label="коло",
                 command=circle)

menu.add_command(label="квадрат",
                 command=circle1)

menu.add_command(label="трикутник",
                 command=circle2)



mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="відкрити...")
filemenu.add_command(label="новий")
filemenu.add_command(label="зберегти...")
filemenu.add_command(label="вихід")

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_cascade(label="допомога", menu=helpmenu2)
helpmenu.add_command(label="про програму")

mainmenu.add_cascade(label="файл", menu=filemenu)
mainmenu.add_cascade(label="довідка", menu=helpmenu)

helpmenu2 = Menu(helpmenu, tearoff=0)
helpmenu2.add_command(label="локальна справа")
helpmenu2.add_command(label="на сайтє")
root.mainloop()

    
