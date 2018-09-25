from Tkinter import *

root = Tk()

labelName=Label(root,text="Username:")
labelPsw=Label(root,text="password:")
entry_name=Entry(root)
entry_psw=Entry(root)

labelName.grid(row=0,sticky=E)
labelPsw.grid(row=1,sticky=E)

entry_name.grid(row=0,column=1)
entry_psw.grid(row=1,column=1)

c = Checkbutton(root,text="Keep me Logged IN")
c.grid(columnspan=2)


root.mainloop()