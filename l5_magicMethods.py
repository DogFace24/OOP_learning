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
        return self.name+" "+self.sur

    def applyRaise(self):
        self.pay *= self.raise_amt #you have to access the class var using the employee class or through the self instance
        self.pay = int(self.pay)

    def displayAll(self):
        print("Full name:", (self.name + " " + self.sur))  
        print("Email:", self.email)
        print("Pay:", self.pay)

    def __repr__(self): #generally returns something that can be pasted directly into the python code
        return "Employee('{}', '{}', {})".format(self.name, self.sur, self.pay)
        #this creates a string that can be directly used to create an employee attribute

    def __str__(self):
        return f"{self.fullName()} - {self.email}"
    
    def __add__(self, emp2):
        return self.pay + emp2.pay 
        #here were making the assumption that both the objs passed in would be employee objects
        #you can call it like this: print(Employee.__add__(e1, e2))
        # or like this: print(e1.__add__(e2))

        #but in reality this is dunder is called when you add 2 objs of employee class together
        #i.e., print(e1+e2)

    def __len__(self):
        return len(self.fullName())

e1 = Employee('Aaditya', 'Sahoo', 50000)
e2 = Employee('Test', 'User', 40000)

#print(e1)  this prints where e1 is stored in memory location. magic methods can be used to do more user friendly stuff
#these spl methods are alco called dunder methods as theyre surrounded by __method__. Double UNDERscore --> DUNDER

#dunder init is a spl method

#common dunder methods are : __repr__ and __str__
#repr is more for debugging and stuff, meant for other devs
#str is just a string representation, meant for end user

print(e1.__repr__())

#if repr method is defined then printing out the instance directly falls back on the repr method
#if both repr and str are defined then str is used when print is called

print(e1)
#print(repr(e1)) #this can be used to see the repr, same for str

#suppose you want to add the salaries of employees you have --> create an __add__ method
print(e1+e2) #or print(Employee.__add__(e1, e2)) or print(e1.__add__(e2))

#if we want to find out the length of the full name of employee --> len method

print(len(e2))