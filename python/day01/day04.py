#employee = {
   # "name": "Bhoopathi",
  #  "job": "Developer",
 #   "salary": 25000
#}

#for key in employee:
 #   print(key)

#employee = {
   # "name": "Bhoopathi",
  #  "job": "Developer",
 #   "salary": 25000
#}

#for key, value in employee.items():
    #print(key, ":", value)


#employee = {
 #   "name": "Bhoopathi",
  #  "age": 24,
   # "salary": 25000
#}

#def show_employee(employee):
 #   print("Name:", employee["name"])
  #  print("Age:", employee["age"])
   # print("Salary:", employee["salary"])

#show_employee(employee)

employees = [
    {"name": "Bhoopathi", "age": 24, "salary": 25000},
    {"name": "Rahul", "age": 17, "salary": 18000},
    {"name": "Priya", "age": 22, "salary": 35000}
]

def employee_check(employee):
    print("Name:", employee["name"])
    print("Age:", employee["age"])
    print("Salary:", employee["salary"])

    if employee["salary"] >= 30000:
        print("High Salary")
    elif employee["salary"] >= 20000:
        print("Medium Salary")
    else:
        print("Low Salary")

for employee in employees:
    employee_check(employee)