class Employee:

    def __init__(self,first,last):
        self.first = first
        self.last = last
    
    def get_data(self):
        print(self.first + '' +self.last)

    def Email(self):
        email = self.first + '.' + self.last + '@company.com'
        return email

# emp1 = Employee() # First instance of class is created

# emp2 = Employee() # Second Instance of class is created

# emp1.name = 'Rajat' # This is instance varibale

# emp2.name = 'Manav' # This is instance varibale

# print(emp1.name)
# print(emp2.name)

emp1 = Employee('Rajat','Prakash')
emp2 = Employee('Manav','Saxena')
# emp1.get_data()
# emp2.get_data()
print(emp1.Email())
print(emp2.Email())