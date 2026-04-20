"""
Python Task-6

Problem 2: Employee Management

Create a base class Employee with attributes like name, salary, and a method calculate_salary().
Inherit from this class to create subclasses RegularEmployee, ContractEmployee, and Manager.
Each subclass should have specific attributes and calculations for salary.

Implement inheritance and polymorphism to calculate the salary of different employee types based
 on their specific attributes and rules.
"""

# Base Class Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary # Private data member salary


    # Get method for salary
    def get_salary(self):
        return self.__salary

    # Set method(Protected method) to update salary internally
    def _set_salary(self, full_salary):
        self.__salary = full_salary

    def calculate_salary(self):
        return self.__salary

# Class RegularEmployee inheriting from base class Employee
class RegularEmployee(Employee):
    def __init__(self, name, basic_pay, hra, bonus):
        super().__init__(name, basic_pay)
        self.basic_pay = basic_pay
        self.hra = hra
        self.bonus = bonus

    def calculate_salary(self):
        return self.basic_pay + self.hra + self.bonus

# Class ContractEmployee inheriting from base class Employee
class ContractEmployee(Employee):
    def __init__(self, name, hourly_wage, hours_worked):
        super().__init__(name, 0)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_wage * self.hours_worked

# Class Manager inheriting from base class Employee
class Manager(Employee):
    def __init__(self, name, basic_pay, hra, bonus, lta):
        super().__init__(name, basic_pay)
        self.basic_pay = basic_pay
        self.hra = hra
        self.bonus = bonus
        self.lta = lta

    def calculate_salary(self):
        return self.basic_pay + self.hra + self.bonus + self.lta


# Creating objects for each employee type
regular_emp = RegularEmployee("Kumar", 8500, 1000, 500)
contract_emp = ContractEmployee("Prarthana", 50, 240)
manager = Manager("Ayush", 12000, 1500, 2000, 3000)

# Dictionary with emp_type as key and emp_obj as values
empType_empObj_dict = {"REGULAR": regular_emp, "CONTRACT": contract_emp, "MANAGER": manager}

# Demonstrating polymorphism
for emp_type, emp_obj in empType_empObj_dict.items():
    print("Employee Type: {}".format(emp_type))
    print("Employee Name: {}".format(emp_obj.name))
    print("Employee Salary: {}".format(emp_obj.calculate_salary()), end='\n' + '-'*30 + '\n')


