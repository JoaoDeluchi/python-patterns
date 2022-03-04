from datetime import datetime
from employee import Employee
from employee_collection import Employees
from department import Department
from department_collection import Departments

TESTEEMPLOYEES = (
    (1, 'Douglas Adams', datetime(1942, 7, 6)),
    (2, 'Sherlock Holmes', datetime(1887, 3, 15)),
    (3, 'Albert Einstein', datetime(1915, 11, 25)),
    (4, 'Theodore Roosevelt', datetime(1867, 8, 1)),
    (5, 'Lula Molusco', datetime(1961, 9, 14)),
)

employees = Employees()

for empid, name, hiredate in TESTEEMPLOYEES:
    employees.add_employee(
        Employee(empid, name, hiredate)
    )

TESTDEPARTMENTS = (
    (101, 'BatCaverna', datetime(1942, 7, 6)),
    (102, 'Casinha do Pluto', datetime(1887, 3, 15)),
    (103, 'Centro de gravidade do Vegeta', datetime(1915, 11, 25)),
    (104, 'Amsterdam', datetime(1867, 8, 1)),
    (105, 'Logo depois do Abacaxi', datetime(1961, 9, 14)),
)


departments = Departments()

for empid, name, data_established in TESTDEPARTMENTS:
    departments.add_department(Department(empid, name, data_established))
