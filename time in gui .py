import datetime
from tkinter import *
"""
makeing a app that shows time when clicked a button
"""
x = datetime.datetime.now()

def show ():
    lblMore = Label(root, text=x, bg="black", fg="yellow")
    lblMore.pack()

def deleted():
    lblMore.delete()



root = Tk()
root.title('time now')
lblMore = Label(root, text=x, bg="black", fg="yellow")
lblMore.pack()

lblMorere = Button(root, text="show time", bg="black", fg="yellow", command = show)
lblMorere.pack()

lblMore1 = Button(root, text="clear all ", bg="black", fg="yellow",command= deleted)
lblMore1.pack()

root.mainloop()
