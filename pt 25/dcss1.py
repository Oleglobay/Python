from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def insert_text():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    text.insert(1.0, s)
    f.close()

def extract_text():
    file_name = fd.asksaveasfilename(
        filetypes=(("TXT files", "*.txt*"),
                   ("HTML file","*.html;*.htm"),
                   ("All files","*.*")))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
    f.write(s)
    f.close()
    
def delete_all():
    ans = mb.askyesno("Question", "Are you sure?")
    if ans:
        text.delete(1.0,END)
    


    
root = Tk()
text = Text(width=50, height=25)
text.grid(columnspan=2)
b1 = Button(text="відкрити", command=insert_text)
b1.grid(row=1, sticky=E)
b2 = Button(text="зберегти", command=extract_text)
b2.grid(row=2, sticky=W)
b3 = Button(text="clean", command=delete_all)
b3.grid(row=3, sticky=E)

root.mainloop()
