from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("250x200")
        self.master.title("My GUI")

        self.grid()

        self.message = Label(self, text = "Hello World!")
        self.message.grid()

frame01 = MyFrame()
frame01.mainloop()