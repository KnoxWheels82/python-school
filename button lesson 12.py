from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("250x200")
        self.master.title("My GUI")
        self.grid()

        self.button_click_here = Button( self, text = "Click Here",
            command = self.click_here_click )
        self.button_click_here.grid()

    def click_here_click(self):
        print ("You did it!" )

frame02 = MyFrame()
frame02.mainloop()