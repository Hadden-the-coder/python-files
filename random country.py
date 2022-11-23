from tkinter import *
import random

root = Tk()

root.title("countries and capitals")
root.geometry("500x500")

countryname =  ["Italy", "UK", "France", "USA", "Russia"]
countrylist = Label(root)
countrylist["text"] = "countryname: " + str(countrylist)

capitalname =  ["Rome", "London", "Paris", "Washington D.C", "Moscow"]
capitallist = Label(root)
capitallist["text"] = "capitalname: " + str(capitallist)
label = Label(root)
def random_number():
    random_number1 = random.randint(0,4)
    print(random_number1)
    randomcountry = countryname[random_number1]
    randomcapital = capitalname[random_number1]
    label["text"] = " You are going to visit " + str(randomcountry) + " whose capital is " + str(randomcapital)
btn1 = Button(root,text = "what country you should visit next", command = random_number)
btn1.place(relx = 0.5, rely = 0.5, anchor = CENTER)

countrylist.place(relx = 0.5, rely = 0.2, anchor = CENTER)
capitallist.place(relx = 0.5, rely = 0.3, anchor = CENTER)
label.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()