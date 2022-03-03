from collections.abc import Iterable
from .abs_tree import AbsTree


class Tree(Iterable, AbsTree):
    def __init__(self, name, members) -> None:
        self._name = name
        self._members = members

    def __iter__(self):
        return iter(self._members)

    @property
    def name(self):
        return self._name

    def accept(self, visitor):
        visitor.visit_tree(self)
        for node in self:
            node.accept(visitor)
