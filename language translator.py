from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry("1080x400")
root.config(bg = "#F2CCC3")
root.title("language translator")

languages = list(LANGUAGES.values())
title_label = Label(root, text = "Language translator")
title_label.place(relx = 0.5, rely = 0.1, anchor = CENTER)

input_label = Label(root, text = "enter text")
input_label.place(relx = 0.02, rely = 0.2, anchor = W)
src_lang = ttk.Combobox(root, values = languages, width = 22, state = "read only")
src_lang.place(relx = 0.13, rely = 0.2, anchor = W)
src_lang.set("english")

output_label = Label(root, text = "output")
output_label.place(relx = 0.81, rely = 0.2, anchor = E)
dest_lang = ttk.Combobox(root, values = languages, width = 22, state = "read only")
dest_lang.place(relx = 0.98, rely = 0.2, anchor = E)
dest_lang.set("choose output language")

input_text = Text(root, font = "arial 10", height = 11, wrap = WORD, padx = 5, pady = 5, width = 60, bg = "#FFFCF9", bd = 0)
input_text.place(relx = 0.02, rely = 0.5, anchor = W)

output_text = Text(root, font = "arial 10", height = 11, wrap = WORD, padx = 5, pady = 5, width = 60, bg = "#FFFCF9", bd = 0)
output_text.place(relx = 0.98, rely = 0.5, anchor = E)

def translate():
    translator = Translator()
    try:
        translated = translator.translate(text = input_text.get(1.0, END), src = src_lang.get(), dest = dest_lang.get())
        output_text.delete(1.0, END)
        output_text.insert(END, translated.text)
        
    except:
        print("try again")

trans_btn = Button(root, text = translate, command = translate)
trans_btn.place(relx = 0.5, rely = 0.85, anchor = CENTER)




root.mainloop()