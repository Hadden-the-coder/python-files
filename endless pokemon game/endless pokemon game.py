from tkinter import *
from PIL import ImageTk, Image
root = Tk()

root.title("endless dice game")
root.geometry("600x400")

root.configure(background = "yellow2")
img = ImageTk.PhotoImage(Image.open("button.jpg"))

player1 = Label(root, text = "player 1", bg = "red", fg = "white")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "player 2", bg = "red", fg = "white")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player1_score_label = Label(root, bg = "red", fg = "white")
player1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player2_score_label = Label(root, bg = "red", fg = "white")
player2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_dice_label = Label(root, bg = "chocolate1", fg = "white")
random_dice_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()
