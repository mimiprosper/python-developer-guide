from tkinter import *


# def onButtonClicked():
#     labelText.set('Text changed on button clicked')
#
#
# root = Tk()
#
# labelText = StringVar()
# labelText.set('myLable')
#
# myLable = Label(root, textvariable=labelText)
# myLable.pack()
#
# myButton = Button(root, text='Button Clicked', command=onButtonClicked)
# myButton.pack()
#
# root.mainloop()

def changeToRed():
    labelText.set('Red')
    myLabel.config(bg='red')


def changeToBlue():
    labelText.set('Blue')
    myLabel.config(bg='blue')


def changeToYellow():
    labelText.set('Yellow')
    myLabel.config(bg='yellow')


root = Tk()

labelText = StringVar()
labelText.set('myLable')

myLabel = Label(root, textvariable=labelText)
myLabel.pack()

myButton = Button(root, text='Red', command=changeToRed).pack()
myButton = Button(root, text='Blue', command=changeToBlue).pack()
myButton = Button(root, text='Yellow', command=changeToYellow).pack()


root.mainloop()
