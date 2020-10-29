from datetime import date

class Employee:
    Company = 'Google'

    def __init__(self,name,age,experience):  # Constructor
        self.name = name
        self.age = age
        self.experience = experience
        print('You are inside the Employee Class')
    
    def Get_Details(self):
        print(f'Employee Name is {self.name}, His age is {self.age} and his experience is {self.experience}')

    def Salary(self,signature):
        print(f'{self.name} Salary is {self.salary} Signautre is : {signature}') # using instance variable 

    # Static Method that doesn't require any self keyword
    @staticmethod
    def Greet():
        print('Hello Sir, Good Morning')

    @staticmethod
    def Current_Date():
        print(f"Today is {date.today()}")





rajat = Employee('yash',23,1000)
rajat.Get_Details()


