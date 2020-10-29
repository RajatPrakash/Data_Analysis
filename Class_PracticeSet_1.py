# Create a class programmer for storing information of few programmers working at microsoft

class Programmer:
    Company = 'Microsoft'

    def __init__(self):
        print(f'Welcome to {Programmer.Company}')
        self.name = input('Enter your Name! ')
        self.experience = float(input('Enter your experience! '))
        self.language = input('Enter The language you are confortable with! ')

    def Get_Details(self):
        print(f'Hi {self.name}')
        print(f'Hi {self.experience}')
        print(f'Hi {self.language}')


obj1 = Programmer()
obj2 = Programmer()
obj3 = Programmer()


print(obj1.Get_Details())
print(obj2.Get_Details())
print(obj3.Get_Details())
