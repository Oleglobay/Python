from tkinter import*
root = Tk()

c = Canvas(root, width=1000, height=1000, bg='white')
c.focus_set()
c.pack()

c.create_line(0,50,1000,50,)
c.create_line(0,100,1000,100,)
c.create_line(0,150,1000,150,)
c.create_line(0,200,1000,200,)
c.create_line(0,250,1000,250,)
c.create_line(0,300,1000,300,)
c.create_line(0,350,1000,350,)
c.create_line(0,400,1000,400,)
c.create_line(0,450,1000,450,)
c.create_line(0,500,1000,500,)
c.create_line(0,550,1000,550,)
c.create_line(0,600,1000,600,)
c.create_line(0,650,1000,650,)
c.create_line(0,700,1000,700,)
c.create_line(0,750,1000,750,)
c.create_line(0,800,1000,800,)
c.create_line(0,850,1000,850,)
c.create_line(0,900,1000,900,)
c.create_line(0,950,1000,950,)

c.create_line(50,0,50,1000,)
c.create_line(100,0,100,1000,)
c.create_line(150,0,150,1000,)
c.create_line(200,0,200,1000,)
c.create_line(250,0,250,1000,)
c.create_line(300,0,300,1000,)
c.create_line(350,0,350,1000,)
c.create_line(400,0,400,1000,)
c.create_line(450,0,450,1000,)
c.create_line(500,0,500,1000,)
c.create_line(550,0,550,1000,)
c.create_line(600,0,600,1000,)
c.create_line(650,0,650,1000,)
c.create_line(700,0,700,1000,)
c.create_line(750,0,750,1000,)
c.create_line(800,0,800,1000,)
c.create_line(850,0,850,1000,)
c.create_line(900,0,900,1000,)
c.create_line(950,0,950,1000,)

ball = c.create_oval(140, 140, 160, 160, fill='blue')
c.bind('<Up>', lambda event: c.move(ball, 0, -5))
c.bind('<Down>', lambda event: c.move(ball, 0, 5))
c.bind('<Left>', lambda event: c.move(ball, -5, 0))
c.bind('<Right>', lambda event: c.move(ball, 5, 0))






root.mainloop()
