#employees = [
 #   {"name": "Bhoopathi", "age": 24, "salary": 40000},
  #  {"name": "Rahul", "age": 18, "salary": 18000},
   # {"name": "Priya", "age": 22, "salary": 35000},
#]

#def show_employee(employee):
 #   print("Name:", employee["name"])
  #  print("Age:", employee["age"])
   # print("Salary:", employee["salary"])

#def find_employee(employees, name):
 #   for employee in employees:
  #      if employee["name"] == name:
   #         return employee

    #return None

#def update_salary(employee, new_salary):
 #   employee["salary"] = new_salary

#employee = find_employee(employees, "Bhoopathi")

#if employee:
 #   update_salary(employee, 45000)
  #  print(employee)

#try:
 #   new_salary = int(input("Enter new salary: "))
  #  update_salary(employee, new_salary)
   # print(employee)
#except ValueError:
 #   print("Please enter a valid salary")

#result = find_employee(employees, "Kumar")
#if result:
 #   print("Employee Found")
  #  print("Name:", result["name"])
   # print("Salary:", result["salary"])
#else:
 #   print("Employee Not Found")


employees = [
    {"name": "Bhoopathi", "age": 24, "salary": 45000},
    {"name": "Rahul", "age": 18, "salary": 18000},
    {"name": "Priya", "age": 22, "salary": 35000},
]

def show_employee(employee):
    print("Name:", employee["name"])
    print("Age:", employee["age"])
    print("Salary:", employee["salary"])

def find_employee(employees, name):
    for employee in employees:
        if employee["name"] == name:
            return employee

    return None

def update_salary(employee, new_salary):
    employee["salary"] = new_salary

def show_high_salary_employees(employees):
    for employee in employees:
        if employee["salary"] >= 30000:
            print(employee["name"])

show_high_salary_employees(employees)

employee = find_employee(employees, "Bhoopathi")

try:
    new_salary = int(input("Enter new salary: "))
    update_salary(employee, new_salary)
    print("Salary Updated")
    show_employee(employee)
except ValueError:
    print("Please enter a valid salary")
