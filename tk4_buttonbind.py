from Tkinter import *

root = Tk()

def leftClick(event):
    print("LEFT")
def middleClick(event):
    prinroot.mainloop()t("MIDDLE BRODA")
def rightClick(event):
    print("RIGHT")

frame = Frame(root, width=300, height=300)
frame.bind("<Button-1>",leftClick)
frame.bind("<Button-2>",middleClick)
frame.bind("<Button-3>",rightClick)


frame.pack()