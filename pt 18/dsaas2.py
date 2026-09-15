from tkinter import*
def buy():
    sell = list(box1.curselection())
    sell.reverse()
    for i in sell:
        box2.insert(END, box1.get())
        box1.delete(i)

def back():
    sell = list(box2.curselection())
    sell.reverse()
    for i in sell:
        box1.insert(END, box2.get())
        box2.delete(i)

def save():
    f = open('buy.txt', 'w')
    f.writelines("\n".join(box2.get(0,END)))
    f.close()
root = Tk()
b1 = Frame()
bM = Frame()
b2 = Frame()
b1.pack(side=LEFT)
bM.pack(side=LEFT, padx=3)
b2.pack(side=LEFT)
box1 = Listbox(b1,selectmode=EXTENDED)
box1.pack(side=RIGHT)
scroll1 = Scrollbar(b1,command=box1.yview)
scroll1.pack(side=RIGHT, fill=Y)
box1.config(yscrollcommand=scroll1.set)
butR = Button(bM, text=">>>", command=buy)
butR.pack()
butL = Button(bM, text="<<<", command=back)
butL.pack()
butS = Button(bM, text="save", command=save)
butS.pack()
box2 = Listbox(b2,selectmode=EXTENDED)
box2.pack(side=LEFT)
scroll2 = Scrollbar(b2,command=box2.yview)
scroll2.pack(side=LEFT, fill=Y)
box2.config(yscrollcommand=scroll2.set)
f = open('shop.txt', 'r')
menu = f.read()
f.close()
listM = menu.split("\n")
for i in listM:
    box1.insert(END, i)
root.mainloop()




