from tkinter import*
root = Tk()

c = Canvas(root, width=200, height=200, bg='white')
c.pack()

c.create_line(25,125,75,175)
c.create_line(125,175,175,125)
c.create_line(175,75,125,25)
c.create_line(25,125,25,75)
c.create_line(25,75,75,25)
c.create_line(125,25,75,25)
c.create_line(175,125,175,75)
c.create_line(75,175,125,175)

root.mainloop()
