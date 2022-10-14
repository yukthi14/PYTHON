
class Employee:
    salary=2500
    increment=2.5
    @property
    def salaryAfterincrement(self):
        return self.salary*self.increment 
    @salaryAfterincrement.setter
    def salaryAfterincrement(self,sal):  #salaryAfterincrement = salary * increment
        self.increment=sal/self.salary
e=Employee()
print(e.salaryAfterincrement)
print(e.increment)
e.salaryAfterincrement=1000
print(e.increment)