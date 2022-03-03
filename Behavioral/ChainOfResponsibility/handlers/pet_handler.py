from .abs_handler import AbsHandler


class PetHandler(AbsHandler):
    def __init__(self) -> None:
        self._successors = []

    def add_successor(self, successor):
        self._successors.append(successor)

    def handle(self, request):
        for suc in self._successors:
            if suc.handle(request):
                break
