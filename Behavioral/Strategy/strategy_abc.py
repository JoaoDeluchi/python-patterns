import abc


class AbsStrategy(abc.ABC):

    @abc.abstractmethod
    def calculate(self, order):
        """calculate shipping cost"""
        pass
