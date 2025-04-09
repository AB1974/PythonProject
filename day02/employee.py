import numbers


class Employee:

    pay_tax = 0.40

    def __init__(self,employee_name, employee_title,employee_salary):
       self.employee_name=employee_name
       self.employee_title=employee_title
       self.employee_salary=employee_salary

    def __str__(self):
        return f'{self.employee_name} {self.employee_title} {self.employee_salary}'

    def work(self):
       return f'{self.employee_name} is working'


@classmethod
def display(self):
    return f"f{self.employee_name}.{Employee.pay_tax}"

Employee1=Employee("aylin","tester",1000000)
Employee2=Employee("engin","tester",1200000)

print(Employee1)
print(Employee2)

print(Employee1.work())








