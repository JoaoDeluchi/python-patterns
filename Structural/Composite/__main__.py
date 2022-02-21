from datetime import date
from tree import Tree
from dateutil.relativedelta import relativedelta
from person import Person


def main():
    hitchhickers = Tree([
        Person('Trillian', date(1996, 12, 21)),
        Person('Arthur', date(1955, 9, 21)),
        Person('Ford', date(1996, 3, 18)),
    ])

    singles = Tree([
        Person('Marvin', date(1991, 1, 1)),
        Person('Slarti', date(1993, 5, 6))
    ])

    loner = Person('Dirk', date(1990, 6, 6))

    tree1 = Tree([hitchhickers])
    tree2 = Tree([singles, loner])
    tree3 = Tree([tree1, tree2])

    for tree in tree1, tree2, tree3:
        oldest = tree.get_oldest()
        age = relativedelta(date.today(), oldest.birthdate)
        print(
            f'Oldest person: {oldest.name}; Age: {age.years}; Moths: {age.months}')


if __name__ == '__main__':
    main()
