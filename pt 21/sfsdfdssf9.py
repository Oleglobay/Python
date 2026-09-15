from tkinter import*
root = Tk()

c = Canvas(root, width=200, height=200, bg='white')
c.pack()

c.create_polygon(25,25,25,150,150,25,fill='black')
c.create_polygon(175,25,25,175,175,175)
root.mainloop()
