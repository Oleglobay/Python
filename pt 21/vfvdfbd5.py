from tkinter import*
root = Tk()

c = Canvas(root, width=200, height=200, bg='white')
c.pack()

c.create_line(50,50,100,0)
c.create_line(150,50,100,0)
c.create_line(150,50,100,0)
c.create_rectangle(50,150,150,50,fill='black')





root.mainloop()
