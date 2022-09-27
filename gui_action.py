from tkinter import *

langas = Tk()

def spaudinti_su_enter():
    print("spausdina paspaudus ENTER...")

def spausdinti_su_kairiu(event):
    print("spausdina paspaudus kairį")

def spaudsinti_su_desiniu(event):
    print("spausdina paspaudus dešinį")

mygtukas = Button(langas, text="spausdinti") # command=spaudinti
mygtukas.bind("<Button-1>", spausdinti_su_kairiu)
mygtukas.bind("<Button-3>", spaudsinti_su_desiniu)
langas.bind("<Return>", lambda event: spaudinti_su_enter())
mygtukas.pack()
langas.mainloop()
