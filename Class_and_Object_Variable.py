class Employee:
    Company_Name = 'Intelegencia'
    Designation = 'Software Engineer'


Rajat = Employee()
Rajat.Company_Name = 'Infosys'

print(Rajat.Company_Name)
print(Rajat.Designation)

print('Values Changed ')
Employee.Company_Name = 'Google' 
Employee.Designation = 'Data Analyst'

print(Rajat.Company_Name)
print(Rajat.Designation)
