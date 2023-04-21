from tkinter import *
from tkinter import filedialog as fd
import hashlib

root = Tk()
root.geometry("250x190")
root.configure(background = "lemon chiffon")

def apply_md5():
    print("md5")
    text_file = fd.askopenfilename(title=" Open Text File", filetypes=(("Text Files", "*.txt"),))
    print(text_file)
    read_file = open(text_file, "R")
    paragraph = read_file.read()
    file_result = hashlib.md5(paragraph.encode())
    file_hexd = file_result.hexdigest()
    print(file_hexd)
    md5_file = open("md5.txt", "w")
    md5_file.write(file_hexd)
    print(file_hexd)
    md5_file.close()
    
    
def apply_sha256():
    print("sha256")
    text_file = fd.askopenfilename(title=" Open Text File", filetypes=(("Text Files", "*.txt"),))
    print(text_file)
    read_file = open(text_file, "R")
    paragraph = read_file.read()
    file_result = hashlib.sha256(paragraph.encode())
    file_hexd = file_result.hexdigest()
    print(file_hexd)
    sha256_file = open("sha256.txt", "w")
    sha256_file.write(file_hexd)
    print(file_hexd)
    sha256_file.close()
    
    
btn = Button(root, text = "apply md5", command = apply_md5, relief = FLAT, bg = "orange2", fg = "white")
btn.place(relx = 0.3, rely = 0.5, anchor = CENTER)    

btn1 = Button(root, text = "apply sha256", command = apply_sha256, relief = FLAT, bg = "orange2", fg = "white")
btn1.place(relx = 0.7, rely = 0.5, anchor = CENTER)  
    
    
root.aminloop()