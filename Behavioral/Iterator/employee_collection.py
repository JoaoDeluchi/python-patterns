from collections.abc import Iterable


class Employees(Iterable):
    _employees = {}
    _headcount = 0

    def add_employee(self, employee):
        self._headcount += 1
        self._employees[self._headcount] = employee

    def __iter__(self):
        return (employee for employee in self._employees.values())
