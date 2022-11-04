from tkinter import *
import random

root = Tk()

root.title("Driving liscence")
root.geometry("500x500")
Label_id = Label(root)
Label_name = Label(root)
Label_dob = Label(root)
Label_pin = Label(root)
Label_address = Label(root)
Label_vehicle_type = Label(root)
def driving_liscense():
    driving_liscense_id = 21435658709
    driving_liscense_name = "Oscar"
    driving_liscense_dob = "November 3rd 1998"
    driving_liscense_pin = 6345346584
    driving_liscense_address = "204 winston LA"
    driving_vehicle_type = "4 wheeler"
    print(driving_liscense_id)
    print(driving_liscense_name)
    print(driving_liscense_dob)
    print(driving_liscense_pin)
    print(driving_liscense_address)
    print(driving_vehicle_type)
    Label_id["text"] = driving_liscense_id
    Label_name["text"] = driving_liscense_name
    Label_dob["text"] = driving_liscense_dob
    Label_pin["text"] = driving_liscense_pin
    Label_address["text"] = driving_liscense_address
    Label_vehicle_type["text"] = driving_vehicle_type
btn = Button(root,text = "show driving liscence", command = driving_liscense)
btn.pack()
Label_id.pack()
Label_name.pack()
Label_dob.pack()
Label_pin.pack()
Label_address.pack()
Label_vehicle_type.pack()

root.mainloop()