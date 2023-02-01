from tkinter import *
from tkinter import messagebox
from tkinter import ttk
root = Tk()
root.geometry("900x600")
root.title("GUI")
    
gui_elements = ["label","button","dropdown"]
dropdown = ttk.Combobox(root, state = "readonly", values = gui_elements)
dropdown.pack()
class CreateElements:
    def __init__(self):
        print("this is create element class")
        
    def CreateLabel(self):
        label = Label(root, text = "a new label is being created using a class",fg = "red")
        label.pack()
    
    def createButton(self):
        class_btn = Button(root, text = "button", command = self.message)
        class_btn.pack(padx = 20, pady = 10)
    
    def createDropdown(self):
        value = [1,2,3,4]
        class_dropdown = ttk.combobox(root,state = "readonly")
        class_dropdown.pack()
        
    def choose(self):
        global dropdown
        element = dropdown.get()
        if (element == "label"):
            self.createLabel()
        elif (element == "button"):
            self.createButton() 
        if (element == "dropdown"):
            self.createDropdown()    
        
    def message(self):
        messagebox.showinfo("showinfo","you clicked the button created using class")

object1 = CreateElements()
btn = Button(root, text = "click to create label and button element", command = object1.choose())
btn.pack(padx = 20, pady = 10)

root.mainloop()