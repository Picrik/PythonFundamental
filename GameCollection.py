# source : inside linux spécial python magazin
# Creating an interface

from tkinter import *

from game import rockpaperscissorV2, hangedmanV2, pokerdice

root = Tk()
root.title ("Mon interface de jeux")

mainframe = Frame(root, height = 200, width = 500)
mainframe.pack_propagate(0)
mainframe.pack(padx = 5, pady = 5)

intro = Label(mainframe, text = '''Bienvenue à la collection de jeux Python. Choisissez à quel jeu vous souhaitez jouer :''')
intro.pack(side = TOP)

rps_button = Button(mainframe, text = "Caillou, Papier, Ciseaux", command = rockpaperscissorV2 .gui)
rps_button.pack()

hm_button = Button(mainframe, text = "Pendu", command = hangedmanV2.gui)
hm_button.pack()

pd_button = Button(mainframe, text = "Poker au dés", command = pokerdice.start)
pd_button.pack()

exit_button = Button(mainframe, text = "Quitter", command = root.destroy)
exit_button.pack(side = BOTTOM)

root.mainloop()
