from tkinter import *
from tkinter import messagebox


def buttonTapped():
    messagebox._show('Message', 'Button Clicked')


root = Tk()
myButton = Button(root, text='click me', command=buttonTapped)
myButton.pack()

root.mainloop()
