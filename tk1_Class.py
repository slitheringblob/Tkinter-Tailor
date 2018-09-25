from Tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        # quitButton=Button(self,text="quit!",command=self.client_exit)
        # quitButton.place(x=10,y=10)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        # file button in menu
        file = Menu(menu)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        # edit button in menu
        edit = Menu(menu)
        edit.add_command(label='Undo')
        menu.add_cascade(label='Edit', menu=edit)

    def client_exit(self):
        exit()


root = Tk()
root.geometry("500x500")
root2=Tk()
root2.geometry("20x20")
labelforroot2=Label(root2,text="This is EZ")
labelforroot2.pack()
app = Window(root)
app2=Window(root2)
root.mainloop()
