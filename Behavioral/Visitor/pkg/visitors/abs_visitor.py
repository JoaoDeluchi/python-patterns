import abc


class AbsVisitor(abc.ABC):
    @abc.abstractmethod
    def visit_person(self):
        pass

    @abc.abstractmethod
    def visit_tree(self):
        pass
