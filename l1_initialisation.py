class Employee():

    def __init__(self, name, sur, pay):
        self.name = name
        self.sur = sur
        self.pay = pay
        self.email = name + '.' + sur + "@company.com"

    #display method
    #you must always pass in self as an argument, then self takes the value whatever instance has called it
    def fullName(self):
        print(self.name, self.sur)
        


e1 = Employee('Aadi', 'Sahoo', 100000) #these are now errors as they need arguments that we defined in init
e2 = Employee('Test', 'User', 20000)

#when we initialise an instance like this, then e1 gets passed as 'self'.
#then e1.name = name, etc.

#print(e1, '\n', e2)

#here employee is a class, e1, e1 are instannces of the class Employee
'''
e1.name = 'Aadi'
e1.sur = 'Sahoo'
e1.email = 'Aadi.Sahoo@company.com'
e1.pay = 100000

#here name, sur, email and pay are the attributes of class employee. but their vals are specific to the instance e1

e2.name = 'Test'
e2.sur = 'User'
e2.email = 'Test.User@company.com'
e2.pay = 200000
'''

#we can find out the values of each

print(e1.email)
print(e2.email)

e2.fullName() #here e2 is passed as the 'self' argument
e1.fullName()

#we can also directly call the function using the class, but then we have to pass in the instance 
Employee.fullName(e1)

#last trial
e3 = Employee('Water', 'Bottle', 1000)
print(e3.email)
e3.fullName()