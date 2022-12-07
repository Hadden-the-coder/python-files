from tkinter import *
import random
root = Tk()

root.title("flying colors")
root.geometry("600x400")


dictionary_colours = {"colours":["red","blue","yellow","green","brown","purple","teal","grey"]}

def changebackground():
    number = random.randint(0,7)
    colour = dictionary_colours["colours"][number]
    root.configure(background = dictionary_colours["colours"][number])
btn = Button(root, text = "change background color", command = changebackground)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
  
root.mainloop()