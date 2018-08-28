import tkinter as tk
import src.gui_parts as mygui


if __name__ == '__main__':
    root = tk.Tk()
    my_gui = mygui.MyFirstGUI(root)
    root.mainloop()

"""
The below does not work... :(
"""
# from multiprocessing import Process
# if __name__ == '__main__':
    
#     processes = []
    
#     # root = tk.Tk()
#     processes.append(Process(target=mygui.MyFirstGUI(tk.Tk())))
#     processes.append(Process(target=mygui.MyFirstGUI_grid(tk.Tk())))
    
#     for process in processes:
#         process.start()
    
#     for process in processes:
#         process.join()

#     pass