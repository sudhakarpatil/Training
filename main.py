class Employee:
    empCount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1

    def displayCount(self):
        print("Total Employee %d" %Employee.empCount)

    def displayEmployee(self):
        print("Name: ",self.name,", Salary: ",self.salary)

emp1=Employee("Sid",5000)
emp2=Employee("Mak",4000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee",Employee.empCount)
print("Thank You !!!")

