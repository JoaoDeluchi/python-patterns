from employee import Employee
from access_controls import AccessControls

EMPLOYEES = {
    1: Employee(1, 'Bob', '4 jul 1994', 80000.00),
    2: Employee(2, 'Carol', '28 may 1992', 85000.00),
    3: Employee(3, 'Ted', '18 feb 1988', 55000.00),
    4: Employee(4, 'Alice', '25 nov 1986', 40000.00),
    101: Employee(101, 'Morgan the manager', '14 mar 1975', 110000.00)
}

ACCESSCONTROL = {
    101: AccessControls(101, True)
}
