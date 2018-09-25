from Tkinter import *

#how to make the Main Dropdown Menu


def doit():
    print("wut u do BRODA")


def exiter():
    exit()


root = Tk()

menu1 = Menu(root)
root.config(menu=menu1)

subMenu = Menu(menu1)
menu1.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="new project...", command=doit)
subMenu.add_command(label="new...", command=doit)
subMenu.add_separator()
subMenu.add_command(label="click tingy to ekjit", command=exiter)

editMenu = Menu(menu1)
menu1.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="tingy",command=doit)

root.mainloop()