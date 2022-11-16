from tkinter import *
import random


root = Tk()

root.title("lucky friend wheel")
root.geometry("500x500")

list_of_items = Label(root)
random_number = Label(root)
listitems = ["chips","bottles","bread","books"]
list_of_items["text"] = str(listitems)
def random_number1():
    random_no = random.randint(0,4)
    random_number["text"] ="put item number" + str(random_no) + "in the bag"
btn = Button(root,text = "selectitem", command = random_number1)
btn.place(relx = 0.4, rely = 0.4, anchor = CENTER)
list_of_items.place(relx = 0.4, rely = 0.3, anchor = CENTER)
random_number.place(relx = 0.4, rely = 0.6, anchor = CENTER)
root.mainloop()