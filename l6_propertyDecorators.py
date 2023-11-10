class Emp():

    def __init__(self, name, sur):
        self.name = name
        self.sur = sur
        #for making the prop decorator you make a function out of it, then remove the email
        #self.email = name+"."+sur+"@company.com"

    @property
    def fullName(self):
        return "{} {}".format(self.name, self.sur)
    
    #you make the setter by using the name of the function <funcname>.setter
    @fullName.setter
    def fullName(self, name):
        self.name, self.sur = name.split(' ')

    @fullName.deleter
    def fullName(self):
        print('\nDeleted name.')
        self.name = None
        self.sur = None
    
    @property
    def email(self):
        return "{}.{}@company.com".format(self.name, self.sur)
    
e1 = Emp('Aaditya', 'Sahoo')

#suppose i change the name from Aaditya to aadi
e1.name = 'aadi'
#the email will still give me Aaditya.Sahoo@company.com
#we can create a method for the email but then every attribute call would need to be cganged to a method call

#so we can use prop decorator, which allows us to use methods in the form of attributes

'''
print(e1.name)
print(e1.email)
print(e1.fullName) # --> as fullName is also a decorator now you dont need to put the parenthesis.
'''


#but now that full name is a property you cant change it like e1.fullName = blahblah
#you have to make a setter for it

e1.fullName = 'Test User' 

#now all the info is passed from just input of full name

print(e1.name)
print(e1.email)
print(e1.fullName)

#we can even create a deleter for the full name if we wanted to do some sort of clean-up.
del e1.fullName #del is used to delete objects
