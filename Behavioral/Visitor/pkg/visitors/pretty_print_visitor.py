from .abs_visitor import AbsVisitor


class PrettyPrintVisitor(AbsVisitor):
    def visit_person(self, person):
        print(f'{person.name} was born on {person.birthdate}')

    def visit_tree(self, tree):
        pass
        print(f'{tree.name} members')
