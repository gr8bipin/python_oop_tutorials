class Employee:
    
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):

    raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        #Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

emp_1 = Employee('Corey', 'Schafer', 50000)
#emp_2 = Employee('Test', 'Employee', 60000)

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

print("------------------------------------------------------------------")

#print(emp_1.email)
#print(emp_2.email)

print("------------------------------------------------------------------")

#print(dev_1.email)
#print(dev_2.email)

print("------------------------------------------------------------------")

#print(help(Developer))

print("------------------------------------------------------------------")

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)

print("------------------------------------------------------------------")

#print(dev_1.email)
#print(dev_1.prog_lang)

print("------------------------------------------------------------------")

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
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
            print('-->', emp.fullname())

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(isinstance(mgr_1, Manager))

print(isinstance(mgr_1, Employee))

print(isinstance(mgr_1, Developer))

print(mgr_1.email)

print(issubclass(Developer, Employee))

print(issubclass(Manager, Employee))

print(issubclass(Manager, Developer))

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

