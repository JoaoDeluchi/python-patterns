import abc


class AbsAdapter(abc.ABC):
    def __init__(self, adaptee) -> None:
        self._adaptee = adaptee

    @property
    def adaptee(self):
        return self._adaptee

    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractproperty
    def address(self):
        pass
