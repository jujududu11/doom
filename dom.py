import motor.py as mo
from tkinter import * as tk
mod=[["",""]*100]
recherche = PhotoImage(file = r"\image\loupe.png")
def recherche():
  pass
def mod():
  root2 = Tk()
  liste = Listbox(root2)
  for i in gange():
    liste.insert(i+1, mod[0][i])
  liste.pack()
  bu = Button(gui, image=rechherche,text="chercher",comande=recherche)
  bu.pack()
  root2.mainloop()
def play():
  pass
def option():
  root.quit()
  mod = Tk.Botton(root,text="mod"command=mod)
  mod.pack()
  retour = Tk.Botton(root,text="retour",command=init)
  retour.pack()
  root = Tk()


  
  root.mainloop()
def quit():
  root.quit()

def init():
  root = Tk()
  bouton1 = PhotoImage(file = r"\image\play.png")
  bouton2 = PhotoImage(file = r"\image\option.png")
  bouton3 = PhotoImage(file = r"\image\quit.png")

  play = Tk.Button(root,image=bouton1,command=play)
  play.pack()

  option = Tk.Button(root,image=bouton2,command=option)
  option.pack()

  quit = Tk.Button(root,image=bouton3,command=quit)
  quit.pack()

  root.mainloop()
