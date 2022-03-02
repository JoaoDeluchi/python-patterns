import abc


class AbsObserver(abc.ABC):
    @abc.abstractmethod
    def update(self, value):
        pass

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        self._kpis.detach(self)

    @abc.abstractmethod
    def __enter__(self, exc_type, exc_value, traceback):
        self._kpis.atach(self)
