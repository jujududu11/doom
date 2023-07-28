import motor.py as mo
from tkinter import * as tk

def play():
  pass
def option():
  root.quit()
  retoure = Tk.Botton(root,text="retour",command=init)
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
  play.pack

  option = Tk.Button(root,image=bouton2,command=option)
  option.pack

  quit = Tk.Button(root,image=bouton3,command=quit)
  quit.pack

  root.mainloop()
