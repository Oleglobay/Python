from tkinter import*

def event_info(event):
    print(type(event))
    print(event)
    print(event.time)
    print(event.x_root)
    print(event.y_root)


def focus():
    





    
root = Tk()
root.bind('<Return>', event_info)
root.mainloop()
