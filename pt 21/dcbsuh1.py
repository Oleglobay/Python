from tkinter import*
root = Tk()

c = Canvas(root, width=200, height=200, bg='white')
c.pack()

c.create_line(10,10,190,50)

root.mainloop()
