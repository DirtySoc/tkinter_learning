        for i in range(0, 9):
            name = 'number_' + str(i) + 'button'
            self.name = Button(master, text=i, command=lambda: self.userInput(i))


# Want to use this to create 9 tkinter button ojects for this gui.
for i in range(9):
    name = f'number_{i}_button'
    self.name = Button(master, text=i, command=lambda: self.userInput(i))

# Instead of this longer way:
self.number_0_button = Button(master, text=i, command=lambda: self.userInput(0))
self.number_1_button = Button(master, text=i, command=lambda: self.userInput(1))
self.number_2_button = Button(master, text=i, command=lambda: self.userInput(2))
self.number_3_button = Button(master, text=i, command=lambda: self.userInput(3))
self.number_4_button = Button(master, text=i, command=lambda: self.userInput(4))
self.number_5_button = Button(master, text=i, command=lambda: self.userInput(5))
self.number_6_button = Button(master, text=i, command=lambda: self.userInput(6))
self.number_7_button = Button(master, text=i, command=lambda: self.userInput(7))
self.number_8_button = Button(master, text=i, command=lambda: self.userInput(8))
self.number_9_button = Button(master, text=i, command=lambda: self.userInput(9))

# Try this instead! - Ease @ EngineerMan Discord
self.numberbuttons = [Button(......) for i in range(9)]
