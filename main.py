# pylint: disable=W0614
from tkinter import *
from tkinter.ttk import *

# from src.gui_parts import MyFirstGUI, MyFirstGUI_binds, MyFirstGUI_grid
# from src.calc import Calculator

class MainView:
    """A GUI for selecting what tutorial GUI you would like to show.
    """
    def __init__(self, master):
        """ 
            Args:
                master: a instance of the toplevel widget from tkinter: 
                        tkinter.Tk()        
        """ 
        self.master = master
        master.title = ("tkinter Tutorials")
        
        # Create widgets...
        self.label = Label(master, text="Welcome to this tutorial. Select a GUI to launch:")
        self.button1 = Button(master, text="MyFirstGUI", command=self.testbutton)
        # self.button1 = Button(master, text="MyFirstGUI", command=lambda: self.testbutton("Button 1 Pressed!"))
        # https://stackoverflow.com/questions/20933639/tkinter-button-events-firing-on-load#20933659
        

        # Add widgets to view...
        self.label.grid()
        self.button1.grid()

    # def testbutton(self, buttonName):
    #     print(buttonName)
    # https://stackoverflow.com/questions/20933639/tkinter-button-events-firing-on-load#20933659
    def testbutton(self):
        print("Button Pressed!")

if __name__ == '__main__':
    root = Tk()
    my_gui = MainView(root)
    root.mainloop()
