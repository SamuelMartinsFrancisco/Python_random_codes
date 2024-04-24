class Employee:
    def __init__(self, name, admissionDate, salary):
        self.name = name
        self.admissionDate = admissionDate
        self.salary = salary

    def __repr__(self):
        return (
                'Nome: ' + self.name + '\n' +
                'Data de admissão: ' + self.admissionDate + '\n' +
                'Salário: ' + str(self.salary)
            )

class Manager(Employee):
    def __init__(self, name, admissionDate, salary, bonus):
        self.bonus = bonus
        salary = ((bonus / 100) * salary) + salary
        Employee.__init__(self, name, admissionDate, salary) 

   ''' def __repr__(self):
        return 'Bônus: ' + str(self.bonus) '''
