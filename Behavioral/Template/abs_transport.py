import abc


class AbsTransport(abc.ABC):
    def __init__(self, destination) -> None:
        self._destination = destination

    def take_trip(self):
        self.start_engine()
        self.leave_terminal()
        self.entertainment()
        self.travel_to_destinantion()
        self.arrive_at_destination()

    @abc.abstractmethod
    def start_engine(self):
        pass

    def leave_terminal(self):
        print('Leaving Terminal')

    @abc.abstractmethod
    def travel_to_destinantion(self):
        print('travelling...')

    def entertainment(self):
        pass

    def arrive_at_destination(self):
        print(f'Arriving at {self._destination}')
