import abc


class AbsPet(abc.ABC):
    def __init__(self, name) -> None:
        self.name = name
        self.mediator = None
