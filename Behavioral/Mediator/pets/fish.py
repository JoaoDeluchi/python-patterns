import random
from .abs_pet import AbsPet


class Fish(AbsPet):
    def __init__(self, name) -> None:
        super().__init__(name)

    def needs_food(self):
        if self.mediator.is_morning():
            print(f'Feed {self.name}')
        else:
            print(f'{self.name} its hungry')

    def is_alive(self):
        return random.randint(0, 1)
