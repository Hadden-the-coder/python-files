from tkinter import *
root = Tk()

root.title("encapsulation")
root.geometry("400x400")

label_name = Label(root, text = "name: ")
label_name.place(relx = 0.3, rely = 0.1, anchor = CENTER)

input_name = Entry(root)
input_name.place(relx = 0.6, rely = 0.1, anchor = CENTER)

label_password = Label(root, text = "password: ")
label_password.place(relx = 0.3, rely = 0.2, anchor = CENTER)

input_password = Entry(root)
input_password.place(relx = 0.6, rely = 0.2, anchor = CENTER)

label_captcha = Label(root, text = "captcha: ")
label_captcha.place(relx = 0.3, rely = 0.3, anchor = CENTER)

input_captcha = Entry(root)
input_captcha.place(relx = 0.6, rely = 0.3, anchor = CENTER)

label_show_name = Label(root)
label_show_name.place(relx = 0.5, rely = 0.7, anchor = CENTER)

label_show_password = Label(root)
label_show_password.place(relx = 0.5, rely = 0.8, anchor = CENTER)

label_show_captcha = Label(root)
label_show_captcha.place(relx = 0.5, rely = 0.9, anchor = CENTER)


class userDB():
    def __init__(self):
        self.__username = "james"
        self.__password = "godzilla10k343"
        self.captcha = "A7B"
        
    def show_user(self):
        label_show_name["text"] = "name: " + self.__username
        label_show_password["text"] = "password: " + self.__password
        label_show_captcha["text"] = "captcha: " + self.captcha
        
        
        
user = userDB()
def adduser():
    global user
    user.username = input_name.get()
    user.password = input_password.get()
    user.captcha = input_captcha.get()
    print("details updated")
    
btn = Button(root, text = "update log in details", command = adduser)
btn.place(relx = 0.3, rely = 0.5, anchor = CENTER)

btn1 = Button(root, text = "show profile", command = user.show_user) 
btn1.place(relx = 0.7, rely = 0.5, anchor = CENTER) 


root.mainloop()
  