from abs_prototype import AbsPrototype
from abs_computer import AbsComputer
import copy


class MainBoard(object):
    manufacturer: str
    model: str

    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model


class Tower(AbsComputer, AbsPrototype):
    def __init__(self, model, mainboard, processor, memory, hard_drive, graphics, monitor):
        self.model = model
        self.mainboard = mainboard
        self.processor = processor
        self.memory = memory
        self.hard_drive = hard_drive
        self.graphics = graphics
        self.monitor = monitor

    def display(self):
        print('Custom Computer: ' + self.model)
        print(f'\t mainboard: {self.mainboard.model}')
        print(f'\t processor: {self.processor}')
        print(f'\t Memory: {self.memory}')
        print(f'\t Hard Drive: {self.hard_drive}')
        print(f'\t graphics: {self.graphics}')
        print(f'\t monitor: {self.monitor if self.monitor else "None"}')

    def clone(self):
        return copy.deepcopy(self)
