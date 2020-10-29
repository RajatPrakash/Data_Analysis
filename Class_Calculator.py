import math

class Calculator:
    def __init__(self):
        self.number = int(input('Number: '))
        print('Welcome to Class Calculator')

    def square(self):
        print(f'Square of number {self.number} is --> {self.number**2}')

    def cube(self):
        print(f'Cube of number {self.number} is --> {self.number**3}')

    def sqroot(self):
        print(f'Square Root  of number {self.number} is --> {math.sqrt(self.number)}')


Obj1 = Calculator()
Obj1.square()
Obj1.cube()
Obj1.sqroot()
