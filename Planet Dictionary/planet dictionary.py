from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
root = Tk()

root.title("Planet Encyclopedia")
root.geometry("500x500")
root.configure(background = "lightblue")

mercury = ImageTk.PhotoImage(Image.open("mercury.jpg"))
venus = ImageTk.PhotoImage(Image.open("venus.jpg"))
earth = ImageTk.PhotoImage(Image.open("earth.jpg"))

label_planet = Label(root,text = "Planet  :", bg = "lightblue")
label_planet_name = Label(root,font = ("courier",18,"bold"),bg = "lightblue")
label_planet_image = Label(root, bg = "gold2", highlightthickness = 5,borderwidth = 2, relief = SOLID)
label_planet_gravity_radius = Label(root,font = ("castellar"), bg = "lightblue")
label_planet_info = Label(root,font = ("courier",18,"bold"),bg = "lightblue",wraplength = 500)

planets = ["mercury","venus","earth"]
selectval = StringVar()
dropdown = ttk.Combobox(root, values = planets, textvariable = selectval)

def Planet_Info():
    planet = selectval.get()
    if planet == "mercury":
        label_planet_name["text"]="mercury"
        label_planet_image["image"]= mercury
        label_planet_gravity_radius["text"]="gravity: 3.7m/s2 \n radius: 2439.7 kilometers"
        label_planet_info["text"]="mercury is the smallest planet in our solar system"
    elif planet == "venus":
        label_planet_name["text"]="venus"
        label_planet_image["image"]= venus
        label_planet_gravity_radius["text"]="gravity: 8.87m/s2 \n radius: 6051.8 kilometers"
        label_planet_info["text"]="venus is the brightest object in the sky after sun. It is also known as evening star"
    elif planet == "earth":
        label_planet_name["text"]="earth"
        label_planet_image["image"]= earth
        label_planet_gravity_radius["text"]="gravity: 9.807m/s2 \n radius: 6371 kilometers"
        label_planet_info["text"]="earth is the only place in the known universe confirmed to have life"
    
btn = Button(root, text = "show planet info", command = Planet_Info)
btn.place(relx=0.5,rely = 0.18, anchor = CENTER)

label_planet.place(relx=0.2,rely = 0.1, anchor = CENTER)
label_planet_name.place(relx=0.5,rely = 0.25, anchor = CENTER)
label_planet_image.place(relx=0.5,rely = 0.5, anchor = CENTER)
label_planet_gravity_radius.place(relx=0.5,rely = 0.8, anchor = CENTER)
label_planet_info.place(relx=0.5,rely = 0.9, anchor = CENTER)
dropdown.place(relx = 0.5, rely = 0.1, anchor = CENTER)

root.mainloop()

