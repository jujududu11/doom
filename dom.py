import motor.py as mo
from tkinter import * as tk

def play():
  pass
def option():
  pass
def quit():
  root.quit()


root = Tk()
bouton1 = PhotoImage(file = r"\image\play.png")
bouton2 = PhotoImage(file = r"\image\option.png")
bouton3 = PhotoImage(file = r"\image\quit.png")

play = Tk.Button(root,bouton1,command=play)
play.pack

option = Tk.Button(root,bouton2,command=option)
option.pack

quit = Tk.Button(root,bouton3,command=quit)
quit.pack

root.mainloop()
