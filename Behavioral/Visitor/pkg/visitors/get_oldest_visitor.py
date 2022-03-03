from .abs_visitor import AbsVisitor
from ..tree.null_person import NullPerson


class GetOldestVisitor(AbsVisitor):
    def __init__(self):
        self.oldest = NullPerson()

    def visit_person(self, person):
        if person.birthdate < self.oldest.birthdate:
            self.oldest = person

    def visit_tree(self, tree):
        pass
