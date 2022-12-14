from tkinter import *
from PIL import ImageTk, Image
import random
root = Tk()

root.title("endless pokemon game")
root.geometry("600x400")

root.configure(background = "yellow2")

button = ImageTk.PhotoImage(Image.open("button.jpg"))
pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
bulbasour = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
charmender = ImageTk.PhotoImage(Image.open("charmender.jpg"))
squirtle = ImageTk.PhotoImage(Image.open("squirtle.jpg"))
ratata = ImageTk.PhotoImage(Image.open("ratata.jpg"))
nidoking = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
meowth = ImageTk.PhotoImage(Image.open("meowth.jpg"))
persion = ImageTk.PhotoImage(Image.open("persion.jpg"))
abra = ImageTk.PhotoImage(Image.open("abra.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
Iyvasour = ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))

listimage = ["abra.jpg", "bulbasour.jpg", "charmender.jpg","Iyvasour.jpg","jigglypuff.jpg","kadabra.jpg","meowth.jpg","nidoking.jpg","paras.jpg","persion.jpg","pikachu.jpg","ratata.jpg","squirtle.jpg"]
listpower = [30,60,50,100,70,70,60,90,40,70,200,40,50]
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

labelimage = Label(root)
labelimage.place(relx = 0.5, rely = 0.6, anchor = CENTER)


player1_score = 0
def player1():
    global player1_score
    random_number = random.randint(0,10)
    random_pokemon = listimage[random_number]
    labelimage["image"] = random_pokemon
    random_power = listpower[random_number]
    labelpower["text"] = random_power
    random_dice_label["text"] = "player1 power " + str(random_power)
    player1_score = player1_score + random_power
    player1_score_label["text"] = str(player1_score)

player_1_btn = Button(root,image = button, command = player1)
player_1_btn.place(relx = 0.1, rely = 0.6, anchor = CENTER)


player2_score = 0
def player2():
    global player2_score
    random_number = random.randint(0,10)
    random_pokemon = listimage[random_number]
    labelimage["image"] = random_pokemon
    random_power = listpower[random_number]
    labelpower["text"] = random_power
    random_dice_label["text"] = "player2 power" + str(random_power)
    player2_score = player2_score + random_power
    player2_score_label["text"] = str(player2_score)

player_2_btn = Button(root,image = button, command = player2)
player_2_btn.place(relx = 0.9, rely = 0.6, anchor = CENTER)



root.mainloop()
