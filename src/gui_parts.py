# pylint: disable=W0614
from tkinter import *
from tkinter.ttk import *

class MyFirstGUI:
    """ A simple GUI to introduce tkinter.
    """
    def __init__(self, master):
        """ 
            Args:
                master: a instance of the toplevel widget from tkinter. 
                tkinter.Tk()        
        """ 
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        #self.greet_button.pack() # By default pack stacks widgets vertically.
        self.greet_button.pack(side=LEFT) # Moves the greet button to the left.

        self.close_button = Button(master, text="Close", command=master.quit)
        #self.close_button.pack() # By default pack stacks widgets vertically.
        self.close_button.pack(side=RIGHT) # Moves the close button to the right.

    def greet(self):
        print("Greetings!")

class MyFirstGUI_grid:
    """ Similar to MyFirstGUI but uses grid to pack widgets.
    """
    def __init__(self, master):
        """ 
            Args:
                master: a instance of the toplevel widget from tkinter. 
                tkinter.Tk()        
        """ 
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        #self.greet_button.pack() # By default pack stacks widgets vertically.
        self.greet_button.pack(side=LEFT) # Moves the greet button to the left.

        self.close_button = Button(master, text="Close", command=master.quit)
        #self.close_button.pack() # By default pack stacks widgets vertically.
        self.close_button.pack(side=RIGHT) # Moves the close button to the right.

    def greet(self):
        print("Greetings!")
if __name__ == '__main__':
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()