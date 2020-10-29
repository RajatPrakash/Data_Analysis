class Employee:
    Company = 'Google'

    def Salary(self):
        print(f'{self.name} Salary is {self.salary}') # using instance variable 


rajat = Employee()
rajat.name = 'Rajat'
rajat.salary = 1000000
rajat.Salary() # interpreted as --- Employee.Salary(rajat) object named is passed as parameter henced self