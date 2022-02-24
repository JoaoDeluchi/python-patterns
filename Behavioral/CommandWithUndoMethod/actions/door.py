class Door(object):
    def __init__(self,  name) -> None:
        self.name = name

    def lock(self):
        print(f'{self.name} is locked')

    def unlock(self):
        print(f'{self.name} is unlocked')
