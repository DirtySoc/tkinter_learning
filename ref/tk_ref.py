import tkinter as tk
import time
from multiprocessing import Process   

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="", width=10)
        self.label.pack()
        self.remaining = 0
        self.countdown(10)
        self.mainloop()

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="time's up!")
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    
    # Below generates a 10 second timer.
    app = ExampleApp()

    # Below generates 4 clock windows all on their own process.
    """
    processes = []

    for i in range(0,4):
        processes.append(Process(target=App))

    for process in processes:
        process.start()

    for process in processes:
        process.join()
    """        