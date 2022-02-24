class Appliance(object):
    def __init__(self,  name) -> None:
        self.name = name

    def on(self):
        print(f'{self.name} has been turned on')

    def off(self):
        print(f'{self.name} has been turned off')
