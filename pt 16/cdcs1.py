from tkinter import*

def insert_text():
    s = "hello world"
    text.insert(1.0, s)
    
def get_text():
    s = text.get(1.0, END)
    label['text'] = s

def delete_text():
    text.delete(1.0, END)

root = Tk()

text = Text(width=25, height=5)
text.pack()

frame = Frame()
frame.pack()

Button(frame, text="paste", command=insert_text).pack(side=LEFT)
Button(frame, text="take", command=get_text).pack(side=LEFT)
Button(frame, text="del", command=delete_text).pack(side=LEFT)
label = Label()
label.pack()
root.mainloop()
