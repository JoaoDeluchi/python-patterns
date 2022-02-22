from .abs_decorator import AbsDecorator


class Inline4Cyl(AbsDecorator):
    @property
    def description(self):
        return self.car.description + ', inline 4 cylinders'

    @property
    def cost(self):
        return self.car.cost + 650.00
