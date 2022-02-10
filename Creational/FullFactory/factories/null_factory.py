from .abs_factory import AbsFactory
from autos.nullcar import NullCar


class NullFactory(AbsFactory):

    def create_auto(self):
        self.null = null = NullCar('Unknown')
        null.name = 'Unknown'
        return null
