#skills1 = {"Python", "HTML", "CSS"}
#skills2 = {"Python", "JavaScript", "React"}

#print(skills1.intersection(skills2))

#employee = {
#    "name": "Bhoopathi",
 #   "details": {
  #      "age": 24,
   #     "job": "Developer",
    #    "salary": 25000,
     #   "experience": 2
#    }
#}

#employee["details"]["salary"] = 30000

#print(employee["details"]["job"])
#print(employee["details"]["salary"])
#print(employee["details"]["experience"])

#employees = [
   # {"name": "Bhoopathi", "age": 24, "salary": 25000},
  #  {"name": "Rahul", "age": 17, "salary": 18000},
 #   {"name": "Priya", "age": 22, "salary": 35000}
#]

#def show_high_salary(employees):
   # for employee in employees:
  #      if employee["salary"] >= 20000:
 #           print(employee["name"], "-", employee["salary"])

#show_high_salary(employees)

#def find_employee(employee):
 #   return employee

#employee = {
 #   "name": "Bhoopathi",
  #  "age": 24,
   # "salary": 25000
#}

#result = find_employee(employee)

#print(result["name"])
#print(result["salary"])

#employees = [
   # {"name": "Bhoopathi", "age": 24, "salary": 25000},
  #  {"name": "Rahul", "age": 17, "salary": 18000},
 #   {"name": "Priya", "age": 22, "salary": 35000}
#]

#def find_employee(employees, name):
 #   for employee in employees:
  #      if employee["name"] == name:
   #         return employee

#result = find_employee(employees, "Rahul")
#print(result["salary"])


#employees = [
 #   {"name": "Bhoopathi", "age": 24, "salary": 25000},
  #  {"name": "Rahul", "age": 17, "salary": 18000},
   # {"name": "Priya", "age": 22, "salary": 35000}
#]

#def find_employee(employees, name):
 #   for employee in employees:
  #      if employee["name"] == name:
   #         return employee

#result = find_employee(employees, "Priya")

#if result:
 #   print("Name:", result["name"])
  #  print("Salary:", result["salary"])
#else:
 #   print("Employee not found")


#Employee Management System

employees = [
    {
        "name": "Bhoopathi",
        "age": 24,
        "salary": 25000,
        "skills": {"Python", "HTML", "CSS"}
    },
    {
        "name": "Rahul",
        "age": 17,
        "salary": 18000,
        "skills": {"Python", "JavaScript"}
    },
    {
        "name": "Priya",
        "age": 22,
        "salary": 35000,
        "skills": {"Python", "React", "CSS"}
    }
]

def show_employee(employee):
    print("Name:", employee["name"])
    print("Age:", employee["age"])
    print("Salary:", employee["salary"])
    print("Skills:", employee["skills"])

    if employee["salary"] >= 30000:
        print("Category: High Salary")
    elif employee["salary"] >= 20000:
        print("Category: Medium Salary")
    else:
        print("Category: Low Salary")

for employee in employees:
    show_employee(employee)

def find_employee(employees, name):
    for employee in employees:
        if employee["name"] == name:
            return employee
        
result = find_employee(employees, "Priya")

if result:
    print("Employee found")
    print("Name:", result["name"])
    print("Salary:", result["salary"])
else:
    print("Employee not found")

def show_python_developers(employees):
    for employee in employees:
        if "Python" in employee["skills"]:
            print(employee["name"])

show_python_developers(employees)