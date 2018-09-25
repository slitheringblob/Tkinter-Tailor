from Tkinter import *
root=Tk()
topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text='btn1',fg='red')
button2 = Button(topFrame, text='btn2',fg='blue')
button3 = Button(topFrame, text='btn3',fg='green')
button4 = Button(bottomFrameottomFrame, text='btn4',fg='purple')

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=TOP)
button4.pack(side=BOTTOM)
root.geometry("500x500")
root.mainloop()