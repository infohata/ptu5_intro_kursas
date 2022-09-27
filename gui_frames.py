from tkinter import Tk, Frame, Button, BOTTOM, LEFT, RIGHT, Y
langas = Tk()
langas.geometry("400x300")
# freimai
virsutinis = Frame(langas)
apatinis = Frame(langas)
# mygtukai freimuose
mygtukas1 = Button(virsutinis, text="Pirmas")
mygtukas2 = Button(virsutinis, text="Antras")
mygtukas3 = Button(virsutinis, text="Trečias")
mygtukas4 = Button(apatinis, text="Paskutinis")
# pakuojam
virsutinis.pack()
apatinis.pack(side=BOTTOM)
mygtukas1.pack(side=LEFT)
mygtukas2.pack(side=LEFT)
mygtukas3.pack(side=LEFT)
mygtukas4.pack(side=BOTTOM, fill=Y)
# paleidziam
langas.mainloop()
