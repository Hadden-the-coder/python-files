from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root = Tk()
root.geometry("600x450")
clock_image = ImageTk.PhotoImage(Image.open("clock.jpg"))

india_label = Label(root, text = "india")
india_label.place(relx = 0.2, rely = 0.05, anchor = CENTER)

india_clock = Label(root)
india_clock["image"] = clock_image
india_clock.place(relx = 0.2, rely = 0.35, anchor = CENTER)

india_time = Label(root)
india_time.place(relx = 0.2, rely = 0.65, anchor = CENTER)



USA_label = Label(root, text = "india")
USA_label.place(relx = 0.7, rely = 0.05, anchor = CENTER)

USA_clock = Label(root)
USA_clock["image"] = clock_image
USA_clock.place(relx = 0.7, rely = 0.35, anchor = CENTER)

USA_time = Label(root)
USA_time.place(relx = 0.7, rely = 0.65, anchor = CENTER)





class India():
    def times(self):
        home = pytz.timezone("Asia/'Kolkata")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        india_time["text"]="time :" + current_time
        india_time.after(200,self.times)
        
class USA():
    def times(self):
        home = pytz.timezone("US/Central")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        USA_time["text"]="time :" + current_time
        USA_time.after(200,self.times)
        

object_india = India()
object_USA = USA()

india_btn = Button(root, text = "Show time", command = object_india.times)
india_btn.place(relx = 0.2, rely = 0.8, anchor = CENTER)

USA_btn = Button(root, text = "Show time", command = object_USA.times)
USA_btn.place(relx = 0.7, rely = 0.8, anchor = CENTER)

root.mainloop()
        
        
        
        
        
        
        
        