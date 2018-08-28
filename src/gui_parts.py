# pylint: disable=W0614
from tkinter import *
from tkinter.ttk import *

class MyFirstGUI:
    """ A simple GUI to introduce tkinter.
    """
    def __init__(self, master):
        """ 
            Args:
                master: a instance of the toplevel widget from tkinter: 
                        tkinter.Tk()        
        """ 
        self.master = master
        master.title("A simple GUI")

        # Create the widgets...
        self.label = Label(master, text="This is our first GUI!")
        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.close_button = Button(master, text="Close", command=master.quit)

        # Add the widgets to the toplevel window with pack...
        self.label.pack()
        #self.greet_button.pack() # By default pack stacks widgets vertically.
        #self.close_button.pack() # By default pack stacks widgets vertically.
        self.greet_button.pack(side=LEFT) # Moves the greet button to the left.
        self.close_button.pack(side=RIGHT) # Moves the close button to the right.


    def greet(self):
        print("Greetings!")

class MyFirstGUI_grid:
    """ Similar to MyFirstGUI but uses grid to pack widgets.
    """
    def __init__(self, master):
        """ 
            Args:
                master: a instance of the toplevel widget from tkinter: 
                        tkinter.Tk()        
        """ 
        self.master = master
        master.title("A simple GUI")

        # Create the widgets...
        self.label = Label(master, text="This is our first GUI!")
        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.close_button = Button(master, text="Close", command=master.quit)

        # Add the widgets to the toplevel windows with grid...
        self.label.grid(columnspan=2, sticky=W)
        self.greet_button.grid(row=1)
        self.close_button.grid(row=1, column=1)

    def greet(self):
        print("Greetings!")

class MyFirstGUI_binds:
    """Similar to MyFirstGUI but includes the bind method to add an event
    handler to the label that is called when the label is clicked with the LMB
    """
    LABEL_TEXT = [
        "This is our first GUI!",
        "Actually, this is our second GUI.",
        "We made it more interesting...",
        "...by making this label interactive.",
        "Go on, click on it again.",
    ]
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        self.label = Label(master, textvariable=self.label_text)
        self.label.bind("<Button-1>", self.cycle_label_text)
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT) # wrap around
        self.label_text.set(self.LABEL_TEXT[self.label_index])

if __name__ == '__main__':
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()