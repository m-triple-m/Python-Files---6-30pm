class Employee:
    hra_per = 10
    da_per = 8
    bonus = 4000

    def __init__(self, name, desig, salary):
        self.name = name
        self.salary = salary
        self.desig = desig

        self.hra, self.da = self.salary*self.hra_per/100, self.salary*self.da_per/100
        self.total = self.salary+self.hra+self.da+self.bonus
    
    def getBasic(self):
        return f"Basic Salary of Empoyee {self.name} : {self.salary}"

    def getTotal(self):
        self.hra, self.da = self.salary*self.hra_per/100, self.salary*self.da_per/100
        self.total = self.salary+self.hra+self.da+self.bonus

        return self.total

    def __repr__(self):
        return f"""
                Employee name : {self.name}
                Designation : {self.desig}
                Basic Salary : {self.salary}
                Total Salary : {self.total}
                """

    def promote(self, desig, increment):
        self.desig = desig
        self.salary+=increment
        print(f'{self.name} got promoted to {self.desig}')


if __name__ == "__main__":
    emp1 = Employee('Mr. Anderson', 'Developer', 23000)

    print(emp1.getBasic())

    print(emp1.getTotal())

    print(emp1)

    emp1.promote('Senior Developer', 6000)

    print(emp1)