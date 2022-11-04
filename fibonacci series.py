from tkinter import*
root = Tk()
root.title("fibonacci")
root.geometry("400x400")

label_series = Label(root,text = "fibonacci series")
label_flower = Label(root)
label_spiral = Label(root)

def Fibonacci():
    num = 10
    first_number = 0
    second_number = 1
    sum = 0
    counter = 1
    while(counter<=num):
        label_series["text"]+=str(sum)+" "
        counter = counter+1
        first_number = second_number
        second_number = sum
        sum = first_number + second_number
    label_flower["text"]="flower is fully bloomed"
    label_spiral["text"]="spirals in right direction are"+ str(first_number)+"and spirals in the left direction are"+ str(second_number)+"\n total spirals are"+ str(sum)

button = Button(root,text = "show fibonacci series",command = Fibonacci)
button.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()
root.mainloop()
      