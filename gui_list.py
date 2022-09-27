from tkinter import *

langas = Tk()

def spausdinti():
    try:
        pasirinkta = sarasas[dezute.curselection()[0]]
    except IndexError:
        label_pasirinkta["text"] = "NIEKO!"
    else:
        label_pasirinkta["text"] = pasirinkta

dezute_scroll = Scrollbar(langas)
# listbox'ui priskiriam scrollbar'ą, listbox'o plotis 5, pasirinkti galima tik po vieną
dezute = Listbox(langas, yscrollcommand=dezute_scroll.set, width=5, selectmode=SINGLE)
# scrollbaro pizicija atsinaujins, prastūmus listbox'ą kitais būdais (ne su scrollbaru)
dezute_scroll.config(command=dezute.yview)
sarasas = range(1983, 2023)
dezute.insert(END, *sarasas)
label_pasirinkta = Label(langas, text="Pasirinkite!")
button_pasirinkti = Button(langas, text="Rinktis", command=spausdinti)
# pack and go
dezute.pack(side=LEFT, fill=Y)
dezute_scroll.pack(side=RIGHT, fill=Y)
button_pasirinkti.pack()
label_pasirinkta.pack()
langas.mainloop()
