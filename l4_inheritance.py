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

e1 = Employee('Aaditya', 'Sahoo', 50000)


class Dev(Employee): #shows that this class inherits from Employee
    raise_amt = 1.10 #were modifyiing the value of only the subclass

    def __init__(self, name, sur, pay, prog_lang = None):
        super().__init__(name, sur, pay) #here we pass in the values to the parent class.
        #you can either do this or say Employee.__init__(self, name, sur, pay)
        if prog_lang is not None:
            self.prog_lang = prog_lang
        else:
            self.prog_lang = "Lmao dont know"

    def PLang(self):
        print(self.prog_lang)

#d1 = Dev('Test', 'Dev', 40000)
#d1.displayAll()

#we can use the help function to find out the data which has been inherited
#print(help(Dev)) 

d1 = Dev('Test', 'Dev', 60000, 'Python')

#d1.applyRaise() #here the default 1.04 value is taken for raise
#print(d1.pay)

#d1.PLang()

class Manager(Employee):

    def __init__(self, name, sur, pay, emp_list = None):
        super().__init__(name, sur, pay)
        if emp_list is None: 
            emp_list = []
        else:
            self.emp_list = emp_list

    def print_emps(self):
        for emp in self.emp_list:
            print('--->', emp.fullName())
        print()

    def add_emp(self, new_emp):
        if new_emp not in self.emp_list:
            self.emp_list.append(new_emp)
            print("New Employee added sucessfully")

    def rem_emp(self, emp_to_rem):
        if emp_to_rem in self.emp_list:
            self.emp_list.remove(emp_to_rem)
            print("Employee removed sucessfully")

m1 = Manager('Manager', 'One', 100000, [e1, d1])

m1.print_emps()

d2 = Dev('Test', 'Dev2', 70000)
m1.add_emp(d2)

m1.print_emps()

m1.rem_emp(d2)

m1.print_emps()