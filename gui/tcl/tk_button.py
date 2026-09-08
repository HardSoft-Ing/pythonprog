import Tkinter as tk
from time import sleep

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.count = 0

    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        self.hi_there["text"] = self.hi_there["text"] + ": " + str(self.count)
        self.count += 1
        # Test: block callback execution to delay button-update. 
        #sleep(1) 
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()