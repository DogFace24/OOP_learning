class Employee():

    raise_amt = 1.04
    num_emps = 0

    def __init__(self, name, sur, pay):
        self.name = name
        self.sur = sur
        self.pay = pay
        self.email = name + '.' + sur + "@company.com"

        #we can increment num_emps everytime the class is initialised to get a count of number of employees
        Employee.num_emps += 1

    def fullName(self):
        print(self.name, self.sur)

    def displayAll(self):
        print("Full name:", (self.name + " " + self.sur))
        print("Email:", self.email)
        print("Pay:", self.pay)

    def applyRaise(self):
        self.pay *= self.raise_amt #you have to access the class var using the employee class or through the self instance
        self.pay = int(self.pay)

    @classmethod #this is a decorator, used to show that the next method is a class method
    def set_raise(cls, amt): #here cls is used to pass in the class/instance of the class, cls is the convention
        cls.raise_amt = amt

    @classmethod
    def fromString(cls, info): #this is the "alternative" constructor, you can directly pass the info as a string
        first, last, pay = info.split("-")
        return cls(first, last, pay) #you need to return this info to whichever variable called it to make it an instance

    @staticmethod
    def isWeekDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return "not a weekday"
        else:
            return "a weekday"
        
    


#print(Employee.num_emps)

e1 = Employee('Aadi', 'Sahoo', 50000)
e2 = Employee('Test', 'User', 40000)

#print(Employee.num_emps)
"""
print(Employee.raise_amt)
print(e1.raise_amt)
print(e2.raise_amt)
"""

#now we can modify the class directly using the class method
Employee.set_raise(1.05) #this will change the raiseamt for all class instances as were directly working with the class
#the above statement is the same as Employee.raise_amt = 1.05

'''print('\n')
print(Employee.raise_amt)
print(e1.raise_amt)
print(e2.raise_amt)
'''

#class methods can be also used as constructors. eg: suppose you want to pass in all the info as a string
'''
emp_3 = "John-Doe-30000"

first, last, pay = emp_3.split("-")
e3 = Employee(first, last, pay)

#this would create a new class instance e3.
#instead you can create a class method which does this task automatically

'''

emp3_info = "Steve-Jobs-300000"
e3 = Employee.fromString(emp3_info)

#now you can access the info of e3 like a normal class instance
e3.displayAll()

#now static methods are basically normal methods, but are included in classes as they have some connection to the class
#static methods dont pass the instance 'self' or the class 'cls'. theyre just regular functions

import datetime

myDate = datetime.date(2023, 11, 6) 
print(f"{myDate} is {Employee.isWeekDay(myDate)}")

#this returns true

yest = datetime.date(2023, 11, 5)
print(f"{yest} is {Employee.isWeekDay(yest)}")