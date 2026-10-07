#List Comprehension

#numbers = []

#for number in range(1, 6):
 #   numbers.append(number)

#print(numbers)

#List Comprehension lets us write the same idea in one line

#numbers = [number for number in range(1, 6)]

#print(numbers)

#Normal loop

#numbers = []

#for number in range(1, 11):
 #   if number % 2 == 0:
  #      numbers.append(number)

#print(numbers)

#List Comprehension version

#numbers = [number for number in range(1, 11) if number % 2 == 0]

#print(numbers)

#Transforming values

#List Comprehensions can also change each item.

#numbers = [number * 2 for number in range(1, 6)]

#print(numbers)

#Filter + transform together

#numbers = [number * 2 for number in range(1, 11) if number % 2 == 0]

#print(numbers)

#employees = [
 #   {"name": "Bhoopathi", "salary": 25000},
  #  {"name": "Rahul", "salary": 18000},
   # {"name": "Priya", "salary": 35000}
#]

#high_salary = [employee["name"] for employee in employees if employee["salary"] >= 20000]

#print(high_salary)

#Dictionary Comprehension

#numbers = [1, 2, 3, 4, 5]

#squares = {number: number * number for number in numbers}

#print(squares)

#numbers = [1, 2, 3, 4, 5, 6]

#even_squares = [number * number for number in numbers if number % 2 == 0]

#print(even_squares)

#numbers = [1, 2, 3, 4, 5]

#result = {number: number * 2 for number in numbers if number > 2}

#print(result)

#employees = [
 #   {"name": "Bhoopathi", "salary": 25000},
  #  {"name": "Rahul", "salary": 18000},
   # {"name": "Priya", "salary": 35000}
#]

#low_salary_names = [employee["name"] for employee in employees if employee["salary"] < 25000]

#print(low_salary_names)

#Dictionary Comprehension

#employees = [
   # {"name": "Bhoopathi", "age": 24, "salary": 25000},
  #  {"name": "Rahul", "age": 17, "salary": 18000},
 #   {"name": "Priya", "age": 22, "salary": 35000}
#]

#adult_names = {employee["name"]: employee["age"] for employee in employees if employee["age"] >= 18}

#print(adult_names)

#Mini-project: Employee Filter

#employees = [
 #   {"name": "Bhoopathi", "age": 24, "salary": 25000},
  #  {"name": "Rahul", "age": 17, "salary": 18000},
   # {"name": "Priya", "age": 22, "salary": 35000},
    #{"name": "Kumar", "age": 28, "salary": 45000}
#]

#high_salary_names = [employee["name"] for employee in employees if employee["salary"] >= 30000]
#medium_salary_names = {employee["name"]: employee["salary"] for employee in employees if employee["salary"] >= 20000}
#adult_with_high_salary = [employee["name"] for employee in employees if employee["salary"] >= 20000 and employee["age"] >= 18]
#adult_employees = {employee["name"]: employee["age"] for employee in employees if employee["age"] >= 18 and employee["salary"] >= 30000}

#print("High Salary:", high_salary_names)
#print("Medium Salary:", medium_salary_names)
#print(adult_with_high_salary)
#print(adult_employees)


employees = [
    {"name": "Bhoopathi", "age": 24, "salary": 25000},
    {"name": "Rahul", "age": 17, "salary": 18000},
    {"name": "Priya", "age": 22, "salary": 35000},
    {"name": "Kumar", "age": 28, "salary": 45000}
]

employee_name = [employee["name"] for employee in employees if employee["age"] < 25 and employee["salary"] >= 20000]

print(employee_name)