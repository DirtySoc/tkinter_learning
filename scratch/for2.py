        for i in range(0, 9):
            name = f'number_{i}button'
            self.name = Button(master, text=i, command=functools.partial(self.userInput, i))