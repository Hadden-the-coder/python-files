from tkinter import *
import speedtest

root = Tk()
root.config(bg = "#dae8f1")
root.title("internet speedtest")
root.geometry("500x300")


label = Label(root, text = "internet speedcheck", font = ("Lucida Sans Unicode", 20, "bold", "italic") ,fg = "#5D6D7E", bg = "#dae8f1")
label.place(relx = 0.5, rely = 0.1, anchor = CENTER)

label_download = Label(root, text = "download speed", font = ("Segoe Print", 18, "bold"), fg = "#1E8449", bg = "#dae8f1")
label_download.place(relx = 0.25, rely = 0.5, anchor = CENTER)

label_upload = Label(root, text = "upload speed", font = ("Segoe Print", 18, "bold"), fg = "#1E8449", bg = "#dae8f1")
label_upload.place(relx = 0.75, rely = 0.5, anchor = CENTER)

label_download_speed = Label(root, font = ("Yu Gothic Light", 14, "bold"), bg = "#dae8f1")
label_download_speed(relx = 0.25, rely = 0.6, anchor = CENTER)

label_upload_speed = Label(root, font = ("Yu Gothic Light", 14, "bold"), bg = "#dae8f1")
label_upload_speed(relx = 0.75, rely = 0.6, anchor = CENTER)

def speedcheck():
    st = speedtest.Speedtest()
    download_speed = round(st.download()/1000000,2)
    label_download_speed["text"] = str(download_speed) + "mbps"
    upload_speed = round(st.upload()/1000000,2)
    label_upload_speed["text"] = str(upload_speed) + "mbps"
btn = Button(root, text = "check speed", command = speedcheck, bg = "#218796", fg = "white", relief = FLAT)
btn.place(relx = 0.5, rely = 0.3, anchor = CENTER)

root.mainloop()