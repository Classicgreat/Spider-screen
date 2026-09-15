from tkinter import Tk, Canvas, ALL, BOTH
from PIL import ImageGrab, Image, ImageTk
from random import randint
from screeninfo import get_monitors

def exitt(event):
    global score
    w.geometry(f"300x100+100+100")
    w.overrideredirect(False)
    c.delete(ALL)
    c.create_text(150, 
                  50, 
                  text=f'Score: {score}', 
                  font=("Helvetica 50 bold"))

def change_pos(event=0):
    global x, y, screenshot, score
    score+=1
    x, y = randint(50, wid-100), randint(50, hei-100)

    w.withdraw()

    c.delete(ALL)
    screenshot = ImageTk.PhotoImage(ImageGrab.grab().crop((x, y, x+100, y+131)))
    c.create_image(0, 0, image=screenshot, anchor='nw')
    c.create_image(0, 0, image=spider_pic, anchor='nw')

    w.geometry(f"+{x}+{y}")
    w.deiconify()
    w.update()

x = 0
y = 0
screen = get_monitors()[0]
wid, hei = screen.width, screen.height
screenshot = 0
score = -1

w = Tk()
w.title("Spider screen")
w.overrideredirect(True)
w.iconbitmap(default="spider.ico")
w.geometry("100x131")
w.attributes('-topmost', True)
w.resizable(width=True, height=False)
w.bind("<Button-3>",exitt)
w.bind("<Button-1>",change_pos)

c=Canvas(w, bd=0, highlightthickness=0)
c.pack(fill=BOTH, expand=True)

spider_pic = ImageTk.PhotoImage(Image.open("spider.ico"))

change_pos()

w.mainloop()