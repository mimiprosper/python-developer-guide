from tkinter import *


def showOnLabel():
    labelText.set(entry.get())


root = Tk()

entry = Entry(root, bg='blue', fg='red')
entry.pack()

button = Button(root, text='Show text on label', command=showOnLabel)
button.pack()


labelText = StringVar()
labelText.set('========')

label = Label(root, textvariable=labelText)
label.pack()

root.mainloop()
