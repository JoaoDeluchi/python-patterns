import abc


class Extend(abc.ABC):
    @abc.abstractproperty
    def expiration_base(self):
        pass
