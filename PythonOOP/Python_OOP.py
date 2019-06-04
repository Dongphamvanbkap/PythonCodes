# Task:
# Create classes to manage human resourse of a company. Class Employee includes description, apply_raise, quit method.
# Class Developer, Manager inherit from Employee Class.

class Employee:

    raise_salary_factor = 1.04
    num_of_employee = 0

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.salary = salary
        # Add to the number of employees.
        Employee.num_of_employee += 1

    def description(self):
        return 'Full name: {} {}\nEmail: {}\nSalary: {}'.format(self.first, self.last, self.email, self.salary)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_salary_factor)
        return self.salary

    def quit(self):
        print('{} {} is going to quit the job.'.format(self.first, self.last))
        # Subtract the number of employees.
        Employee.num_of_employee -= 1


class Developer(Employee):
    raise_salary_factor = 1.10

    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.prog_lang = prog_lang


class Manager(Employee):
    raise_salary_factor = 1.15

    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.description())

emp_1 = Employee('Kurt', 'Wright', 30000)
emp_2 = Employee('Neil', 'Patterson', 35000)

dev_1 = Developer('John', 'Davis', 60000, 'Python')
dev_2 = Developer('Neil', 'Steve', 50000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])


print(dev_1.description())
print(dev_1.apply_raise())

print(emp_1.num_of_employee)

dev_1.quit()
print(dev_1.num_of_employee)
