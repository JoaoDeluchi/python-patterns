import copy
from abs_computer import AbsComputer
from abs_prototype import AbsPrototype


class Laptop(AbsComputer, AbsPrototype):
    def __init__(self, model, processor, memory, hard_drive, graphics, screen):
        self.model = model
        self.processor = processor
        self.memory = memory
        self.hard_drive = hard_drive
        self.graphics = graphics
        self.screen = screen

    def display(self):
        print('Custom Computer: ' + self.model)
        print(f'\t processor: {self.processor}')
        print(f'\t Memory: {self.memory}')
        print(f'\t Hard Drive: {self.hard_drive}')
        print(f'\t graphics: {self.graphics}')
        print(f'\t screen: {self.screen}')

    def clone(self):
        return copy.copy(self)
