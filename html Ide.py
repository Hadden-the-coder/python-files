from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import webbrowser
from tkinter import messagebox
root = Tk()

root.minsize(650,650)
root.maxsize(650,650)

open_image = ImageTk.PhotoImage(Image.open("open.png"))
save_image = ImageTk.PhotoImage(Image.open("save.png"))

run_image = ImageTk.PhotoImage(Image.open("run.png"))

label_file_name = Label(root, text = "file space name")
label_file_name.place(relx = 0.28, rely = 0.03, anchor = CENTER)

input_file_name = Entry(root)
input_file_name.place(relx = 0.46, rely = 0.03, anchor = CENTER)

my_text = Text(root, height = 35, width = 80, bg = "slate gray", fg = "white")
my_text.place(relx = 0.5, rely = 0.55, anchor = CENTER)

name = ""
def openFile():
    global name
    my_text.delete(1.0, END)
    input_file_name.delete(0,END)
    html_file = filedialog.askopenfilename(title="Open html File",filetypes=(("html Files","*.html"),))
    print(html_file)
    name = os.path.basename(html_file)
    formatted_name=name.split('.')[0]
    input_file_name.insert(END,formatted_name)
    root.title(formatted_name)
    html_file = open(name,'r')
    paragraph = html_file.read()
    my_text.insert(END,paragraph)
    html_file.close()

def saveFile():
    input_name = input_file_name.get()
    file = open(input_name + ".html", "w")
    data = my_text.get("1.0", END)
    print(data)
    file.write(data)
    input_file_name.delete(0,END)
    my_text.delete(1.0,END)
    messagebox.showinfo("update", "success")
    
def run_html_file():
    global name
    webbrowser.open(name)


open_button = Button(root, image = open_image, text = "openfile", command = openFile)
open_button.place(relx = 0.05, rely = 0.03, anchor = CENTER)
save_button = Button(root, image = save_image, text = "savefile", command = saveFile)
save_button.place(relx = 0.11, rely = 0.03, anchor = CENTER)
run_button = Button(root, image = run_image, text = "runfile", command = run_html_file)
run_button.place(relx = 0.17, rely = 0.03, anchor = CENTER)



root.mainloop()