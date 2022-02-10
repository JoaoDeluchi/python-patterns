from factories.abs_factory import AbsFactory
from autos.gm.cadillac import CadillacCTS
from autos.gm.camaro import ChevyCamaro
from autos.gm.spark import ChevySpark


class GMFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return ChevySpark()

    @staticmethod
    def create_sport():
        return ChevyCamaro()

    @staticmethod
    def create_luxury():
        return CadillacCTS()
