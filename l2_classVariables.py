class Employee():

    RAISE = 1.04
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

    def applyRaise(self):
        self.pay *= self.RAISE #you have to access the class var using the employee class or through the self instance
        self.pay = int(self.pay)


print("Number of employees:", Employee.num_emps)

e1 = Employee('Aadi', 'Sahoo', 100000)
e2 = Employee('Test', 'User', 1000)

print(e1.pay)
e1.applyRaise()
print("e1 raised by", Employee.RAISE) 
print(e1.pay)


#you can have personalized class variables for each instance

print(Employee.RAISE)
print(e1.RAISE)
print(e2.RAISE)

e1.RAISE = 1.5
#after this change the default value of raise remains the same in employee, but the raise value of e1 is changed

print('\nNew Raises')
print(Employee.RAISE)
print(e1.RAISE)
print(e2.RAISE)

print('\nApplying raise to e1 after new raise')
e1.applyRaise()
print(e1.pay)

e1.pay = 100000 #this was the starting value.
#suppose we want to find the value of e1's pay after 10 years

for i in range(10):
    e1.applyRaise()
    print(f'Year {i+1}: {e1.pay}')

print('Pay of e1 after 10 years:', e1.pay)

print("Number of employees:", Employee.num_emps)