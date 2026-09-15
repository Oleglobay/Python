from tkinter import*
root = Tk()

c = Canvas(root, width=200, height=200, bg='white')
c.pack()

c.create_line(50,50,150,50)
c.create_line(50,25,150,25)
c.create_line(50,75,150,75)
c.create_line(50,100,150,100)
c.create_line(50,125,150,125)
c.create_line(50,150,150,150)
c.create_line(50,175,150,175)
root.mainloop()
