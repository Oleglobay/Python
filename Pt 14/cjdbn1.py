from tkinter import*

root = Tk()

def collr():
    xol.config(text ="#ff0000")
def collo():
    xol.config(text ="#ff7d00")
def colly():
    xol.config(text ="#ffff00")
def collg():
    xol.config(text ="#00ff00")
def colla():
    xol.config(text ="#007dff")
def collb():
    xol.config(text ="#0000ff")
def collf():
    xol.config(text ="#7d00ff")


b1 = Button(text="...", bg="#ff0000", command=collr, bd='20')
b2 = Button(text="...", bg="#ff7d00", command=collo, bd='20')
b3 = Button(text="...", bg="#ffff00", command=colly, bd='20')
b4 = Button(text="...", bg="#00ff00", command=collg, bd='20')
b5 = Button(text="...", bg="#007dff", command=colla, bd='20')
b6 = Button(text="...", bg="#0000ff", command=collb, bd='20')
b7 = Button(text="...", bg="#7d00ff", command=collf, bd='20')
xol = Label(bd='20')

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()
xol.pack()

root.mainloop()
