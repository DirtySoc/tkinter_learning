import tkinter as tk
import src.gui_parts as mygui

if __name__ == '__main__':
    root = tk.Tk()
    my_gui = mygui.MyFirstGUI(root)
    root.mainloop()
    root.destroy()
    pass