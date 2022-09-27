from tkinter import Tk, Label

# sukuriam lango objekta pagal Tk() klasę
langas = Tk()
# nustatom lango dydį
langas.geometry("500x300")
# į langą sukuriam `uzrasas` objektą pagal Label klasę, su tekstu
uzrasas = Label(langas, text="Sveiki, studentai!")
uzrasas2 = Label(langas, text="Smagus antradienis")
# supkauojam uzrasas
uzrasas.pack()
uzrasas2.pack(side='bottom')
# paleidžiam lango programą
langas.mainloop()
