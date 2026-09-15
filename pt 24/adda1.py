from tkinter import *
root = Tk()

Label(text="name:").grid(row=0, column=0, sticky=W, pady=10, padx=10)

table_name = Entry()
table_name.grid(row=0, column=1, columnspan=3,sticky=W+E, padx=10)

Label(text="Row:").grid(row=1, column=0, sticky=W,padx=10, pady=10)

Spinbox(width=7, from_=1, to=50).grid(row=1, column=1, padx=10)

Label(text="col:").grid(row=1, column=2, sticky=E)

Spinbox(width=7, from_=1, to=100).grid(row=1, column=3, sticky=E, padx=10)

Button(text="info").grid(row=2, column=0, pady=10, padx=10)
Button(text="Insert").grid(row=2, column=2)
Button(text="cancel").grid(row=2, column=3,padx=10)

root.mainloop()
