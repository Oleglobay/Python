from tkinter import*
root = Tk()

c = Canvas(root, width=200, height=200, bg='white')
c.pack()

c.create_line(50,50,100,100)
c.create_line(100,100,150,50)

c.create_polygon(100,100,50,150,150,150,fill='black')


root.mainloop()
