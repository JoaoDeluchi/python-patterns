import abc


class AbsTree(abc.ABC):
    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractproperty
    def accept(self):
        pass
