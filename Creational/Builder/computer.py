class Computer(object):
    case: str
    mainboard: str
    cpu: str
    memory: str
    hard_drive: str
    video_card: str

    def display(self):
        print('Custom Computer')
        print(f'\t Case: {self.case}')
        print(f'\t Mainboard: {self.mainboard}')
        print(f'\t CPU: {self.cpu}')
        print(f'\t Memory: {self.memory}')
        print(f'\t Hard Drive: {self.hard_drive}')
        print(f'\t Video Card: {self.video_card}')
