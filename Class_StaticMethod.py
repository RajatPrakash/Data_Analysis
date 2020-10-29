from datetime import date

class Employee:
    Company = 'Google'

    def Salary(self,signature):
        print(f'{self.name} Salary is {self.salary} Signautre is : {signature}') # using instance variable 

    # Static Method that doesn't require any self keyword
    @staticmethod
    def Greet():
        print('Hello Sir, Good Morning')

    @staticmethod
    def Current_Date():
        print(f"Today is {date.today()}")


rajat = Employee()
rajat.name = 'Rajat'
rajat.salary = 1000000

rajat.Salary('RP') # interpreted as --- Employee.Salary(rajat) object named is passed as parameter henced self

rajat.Greet() # Employee.Greet() now it does not required any self keyword 

rajat.Current_Date()