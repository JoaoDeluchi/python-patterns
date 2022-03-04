from collections.abc import Iterable


class Departments(Iterable):
    _departments = []

    def add_department(self, department):
        self._departments.append(department)

    def __iter__(self):
        return (department for department in self._departments)
