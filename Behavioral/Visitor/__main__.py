from datetime import date
from dateutil.relativedelta import relativedelta
from pkg.visitors.get_oldest_visitor import GetOldestVisitor
from pkg.visitors.pretty_print_visitor import PrettyPrintVisitor
from pkg.tree.person import Person
from pkg.tree.tree import Tree

# p = Person('Douglas', date(1952, 3, 11))
# v = PrettyPrintVisitor()
# p.accept(v)


hitchhickers = Tree('Cast', [
    Person('Trillian', date(1996, 12, 21)),
    Person('Arthur', date(1955, 9, 21)),
    Person('Ford', date(1996, 3, 18)),
])

singles = Tree('Characters', [
    Person('Marvin', date(1991, 1, 1)),
    Person('Slarti', date(1993, 5, 6))
])

loner = Person('Dirk', date(1990, 6, 6))

tree1 = Tree('Cast', [hitchhickers])
tree2 = Tree('Others', [singles, loner])
tree3 = Tree('Everyone', [tree1, tree2])

get_oldest = GetOldestVisitor()
tree3.accept(get_oldest)
name, age = get_oldest.oldest.name, relativedelta(
    date.today(), get_oldest.oldest.birthdate)

print(
    f'Oldest Person in tree {tree3.name}: name: {name} age: {age.years} years, {age.months} months')
