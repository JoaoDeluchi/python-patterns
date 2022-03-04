from .abs_pet import AbsPet


class Dog(AbsPet):
    def __init__(self, name) -> None:
        super().__init__(name)

    def wants_walk(self):
        if self.mediator.is_cat_asleep():
            print(f'walk {self.name}')
        else:
            print(f'wake up {self.name}')
            self.mediator.wake_up_cat()
