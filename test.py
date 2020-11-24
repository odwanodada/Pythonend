
from tkinter import *
from random import sample

#Creating a window
from tkinter import *
from random import sample
import random

def response():
    num1.configure(text=str(random.sample(range(1, 49),1)))
    num2.configure(text=str(random.sample(range(1, 49), 1)))
    num3.configure(text=str(random.sample(range(1, 49), 1)))
    num4.configure(text=str(random.sample(range(1, 49), 1)))
    num5.configure(text=str(random.sample(range(1, 49), 1)))
    num6.configure(text=str(random.sample(range(1, 49), 1)))

    output.insert(END,text_display)

def die():
    num1.configure(text=str())
    num2.configure(text=str())
    num3.configure(text=str(0))
    num4.configure(text=str(0))
    num5.configure(text=str(0))
    num6.configure(text=str(0))





#Creating a window
window = Tk()
window.title("6 Figure Lottery!!!")
window.resizable(1000, 2000)
#creating the labels
num1 = Label(window, relief='groove', width = 5, bd=4, text=" ", fg='white', bg='blue')
num1.grid(row = 1, column = 1, padx = 5, pady = 7)
num2 = Label(window, relief='groove', width = 5, bd=4, text=" ", fg='white', bg='blue')
num2.grid(row = 1, column = 2, padx = 5, pady = 7)
num3 = Label(window, relief='groove', width = 5, bd=4, text=" ", fg='white', bg='blue')
num3.grid(row = 1, column = 3, padx = 5, pady = 7)
num4 = Label(window, relief='groove', width = 5, bd=4, text=" ", fg='white', bg='blue')
num4.grid(row = 1, column = 4, padx = 5, pady = 7)
num5 = Label(window, relief='groove', width = 5, bd=4, text=" ", fg='white', bg='blue')
num5.grid(row = 1, column = 5, padx = 5, pady = 7)
num6 = Label(window, width = 5, bd=4, text=" ", fg='white', bg='blue')
num6.grid(row = 1, column = 6, padx = 5, pady = 7)



#Creating a button
#Close
closeButton = Button(window)
closeButton.configure(text = "CLOSE", fg = 'white', bg = '#ff0000')
closeButton.grid(row = 3, column = 1, columnspan = 6, pady = 7)
#Generate Numbers
numberGen = Button(window, width=20, text="Generate Numbers", command=response)
numberGen.configure(fg = "White" ,bg = "Green")
numberGen.grid(row = 2, column = 1, padx = 5, pady = 7)
#Reset
reset = Button(window, width=10, text="Reset", command =die)
reset.configure(fg = "White" ,bg = "Green")
reset.grid(row = 2, column = 2, padx = 5, pady = 7)

#defining a function to close the program
def close():
    quit()



#attaching the "close" function to the "close" button
closeButton.configure(command = close)

#This is the line that runs the program until you exit
window.mainloop()
