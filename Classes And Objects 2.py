import logging

logging.basicConfig(filename='Class.log', level='INFO')

class Employee:

    def __init__(self):
        self.first = input('\nEnter First Name: ')
        self.last = input('Enter Last Name: ')
        self.designation = input('Enter designation: ')  
        logging.info(f'First Name {self.first}')  
        logging.info(f'Last Name {self.last}')  
        logging.info(f'Designation {self.designation}')  
        logging.info(f'Email {self.first}.{self.last}@company.com')                  
        
    def Display(self):
        print(f'\nFirst Name {self.first}')  
        print(f'Last Name {self.last}')  
        print(f'Designation {self.designation}')  
        print(f'Email {self.first}.{self.last}@company.com')  
    

emp1 = Employee().Display()
emp2 = Employee().Display()


