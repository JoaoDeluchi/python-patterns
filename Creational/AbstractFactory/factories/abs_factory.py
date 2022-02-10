import abc


class AbsFactory(abc.ABC):

    @abc.abstractstaticmethod
    def create_economy(self):
        pass

    
    @abc.abstractstaticmethod
    def create_sport(self):
        pass

    
    @abc.abstractstaticmethod
    def create_luxury(self):
        pass
