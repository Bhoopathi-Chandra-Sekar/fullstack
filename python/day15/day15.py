#Module - A module is simply a Python file contatining reusable code.

#from employee import show_employee

#show_employee() #The dot . means: Go inside the employee module and use show_employee.

#import math

#print(math.sqrt(25))

#random module

#Python's random module can generate random values

#import random

#number = random.randint(1, 10)

#print(number)

#Packages - A package is basically a folder that contains related python modules

from company.employee import show_employee
from company.salary import show_salary

show_employee()
show_salary(30000)