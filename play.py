from tkinter import *
from tkinter import messagebox


window = Tk()
window.title("Lotto")
window.geometry("400x400")
window.config(bg="pink")


def verify():
    messagebox.showinfo("you guys are crazy")
    mycheck=Button(window, text="check status", command=verify)
    mycheck.pack()





#Label is for output the results will be display there
num1 = Text(window, width=2, height=1, bg="white",font=("arial", 20, "bold"))
num1.place(x=30,y=50)


num2 = Text(window, width=2, height=1, bg="white",font=("arial", 20, "bold"))
num2.place(x=80,y=50)


num3 = Text(window, width=2, height=1, bg="white",font=("arial", 20, "bold"))
num3.place(x=130,y=50)


num4 = Text(window, width=2, height=1, bg="white",font=("arial", 20, "bold"))
num4.place(x=180,y=50)


num5 = Text(window, width=2, height=1, bg="white",font=("arial", 20, "bold"))
num5.place(x=230,y=50)


num6 = Text(window, width=2, height=1, bg="white",font=("arial", 20, "bold"))
num6.place(x=280,y=50)




window.mainloop()
