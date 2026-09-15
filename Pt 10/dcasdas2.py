from tkinter import *
root = Tk ( )

ent1 = Entry ( width = 20 )
ent1. pack ( )

ent2 = Entry ( width = 20 )
ent2. pack ( )


but1 = Button  (width = 16 ,text = "+")
but1. pack ( )

but2 = Button ( width = 16,text = "-" )
but2. pack ( )

but3 = Button ( width = 16,text = "*" )
but3. pack ( )

but4 = Button ( width = 16,text = "/" )
but4. pack ( )

output = Label(width = 16)
output.pack()

def chekF(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
def dodav(event):
    a = ent1.get()
    b = ent2.get()
    if (chekF())




