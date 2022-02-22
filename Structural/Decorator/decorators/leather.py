from .abs_decorator import AbsDecorator


class Leather(AbsDecorator):
    @property
    def description(self):
        return self.car.description + ', top grain leather'

    @property
    def cost(self):
        return self.car.cost + 3100.00
