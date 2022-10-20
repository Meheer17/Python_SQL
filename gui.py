import function

from tkinter import *
from tkinter import ttk

root = Tk()

widgets = []

root.geometry("640x480")

my_string = StringVar()
my_string.set("HELLO WORLD")

widgets.append(ttk.Label(root, textvariable = my_string))
widgets.append(ttk.Button(root, text = "BUTTON PLACEHOLDER"))

for widget in widgets:
    widget.pack()

root.mainloop()
