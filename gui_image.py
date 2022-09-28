from tkinter import *
from PIL import ImageTk, Image

langas = Tk()
tiltas = ImageTk.PhotoImage(Image.open("img/pont_au_mousson.jpg"))
panel = Label(langas, image=tiltas)
panel.pack(side=BOTTOM, fill=BOTH, expand=YES)
langas.mainloop()