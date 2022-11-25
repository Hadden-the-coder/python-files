from tkinter import *
import random

root = Tk()

root.title("password generator")
root.geometry("500x500")

label = Label(root)
inputbox = Entry(root)
inputbox.place(relx = 0.5, rely = 0.4, anchor = CENTER)
label_guest_password = Label(root)
label_guest_password.place(relx = 0.5, rely = 0.5, anchor = CENTER)

array_3d = [[["1","2","3","4","5","6"],["head","tail"],["A","B","C","D","E","F","G","H"]]]
print(array_3d[0][2][3])
def check_password():
    random_number1 = random.randint(0,5)
    random_number2 = random.randint(0,1)
    random_number3 = random.randint(0,7)
    guestpassword = inputbox.get()
    label_guest_password["text"] = "guessed password = "+ guestpassword
    
    letter1 = str(array_3d[0][0][random_number1])
    letter2 = (array_3d[0][1][random_number2])
    letter3 = array_3d[0][2][random_number3]
    label["text"] = letter1 +""+ letter2 +""+letter3
    password = letter1 +""+ letter2 +""+letter3
    if guestpassword == password:
        print("Correct!")
    else:
        print("Wrong!")
    
btn = Button(root, text = "New password", command = check_password)
btn.place(relx = 0.5, rely = 0.65, anchor = CENTER)
label.place(relx = 0.5, rely = 0.8, anchor = CENTER)

root.mainloop()