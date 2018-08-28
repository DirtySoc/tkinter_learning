"""

# 0 = stopped; 1 = running
swStatus = 0
startTime = 0

def toggleClock():
    if swStatus == 0:
        swStatus = 1
        startTime = time.time()
    else:
        swStatus = 0

    return

def resetOrLap():
    return

# Top level window...
top =tk.Tk()

# Code to add widgets goes here...

# Configure widgets:
titleLable = tk.Label(top, text="Welcome to your clock!")
startStopButton = tk.Button(top, text="Start/Stop", command=toggleClock())
resetButton = tk.Button(top, text="Reset/Lap", command=resetOrLap())
# Pack widgets into top:
titleLable.pack()
startStopButton.pack()
resetButton.pack()
# Start GUI:
top.mainloop()

"""