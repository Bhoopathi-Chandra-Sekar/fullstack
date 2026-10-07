#import json

#with open("employee.json", "r") as file:
#    employee = json.load(file)

#print(employee["name"])
#print(employee["age"])
#print(employee["salary"])

#employee2 = {
 #   "name": "Rahul",
  #  "age": 17,
   # "salary": 18000
#}

#with open("employee2.json", "w") as file:
 #   json.dump(employee2, file, indent=4)

#import json

#employees = [
 #   {
  #      "name": "Bhoopathi",
   #     "age": 24,
    #    "salary": 25000
    #},
    #{
     #   "name": "Rahul",
      #  "age": 17,
       # "salary": 18000
    #},
    #{
     #   "name": "Priya",
      #  "age": 22,
       # "salary": 35000
    #}
#]

#with open("employees.json", "w") as file:
 #   json.dump(employees, file, indent=4)        #json.dump() - python - JSON

#with open("employees.json", "r") as file:
 #   employees_data = json.load(file)            #json.load() - JSON - python

#for employee in employees_data:
 #   if employee["salary"] >= 20000:
  #      print("Name:", employee["name"])
   #     print("Salary:", employee["salary"])

#import json

#with open("employees.json", "r") as file:
 #   employees = json.load(file)

#def show_high_salary(employees):
 #   print("High Salary Employees:")

  #  for employee in employees:
   #     if employee["salary"] >= 30000:
    #        print(employee["name"])

#show_high_salary(employees)

import json

with open("employees.json", "r") as file:
    employees = json.load(file)

def find_employee(employees, name):
    found = False

    for employee in employees:
        if employee["name"] == name:
            print("Employee Found")
            print("Name:", employee["name"])
            print("Age:", employee["age"])
            print("Salary:", employee["salary"])
            found = True
            break

    if found == False:
        print("Employee Not Found")

find_employee(employees, "Priya")
find_employee(employees, "Kumar")