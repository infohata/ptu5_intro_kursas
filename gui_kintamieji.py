from tkinter import *

langas = Tk()

tekstas = StringVar()

def tekstas_save():
    tekstas.set(e_tekstas.get())
    e_tekstas.delete(0, len(e_tekstas.get()))

def tekstas_load():
    l_tekstas["text"] = tekstas.get()

def tekstas_clear():
    # tekstas.set("")
    l_tekstas["text"] = ""
    e_tekstas.delete(0, len(e_tekstas.get()))

e_tekstas = Entry(langas)
l_tekstas = Label(langas, text="")
m_save = Button(langas, text="save", command=tekstas_save)
m_load = Button(langas, text="load", command=tekstas_load)
m_clear = Button(langas, text="clear", command=tekstas_clear)
langas.bind("<Return>", lambda event: tekstas_save())

e_tekstas.pack()
l_tekstas.pack(side=BOTTOM)
m_save.pack(side=LEFT)
m_load.pack(side=LEFT)
m_clear.pack(side=LEFT)

langas.mainloop()
