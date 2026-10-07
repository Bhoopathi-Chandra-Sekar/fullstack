#square = lambda a: a * a    #A lambda is a small function written in one line
#print(square(5))

#map() is used when you want to perform the same operation on every item in a list

#numbers = [1, 2, 3, 4, 5]

#squares = list(map(lambda number: number * number, numbers))

#print(squares)

#numbers = [10, 20, 30, 40]

#add = list(map(lambda number: number + 5, numbers))

#print(add)

#filter() - selects items that satisfy a condition
#map() - changes every item

#numbers = [10, 15, 20, 25, 30]

#even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

#print(even_numbers)

#numbers = [10, 15, 20, 25, 30, 35, 40]

#greater_number = list(filter(lambda number: number > 25, numbers))

#print(greater_number)

#sorted() with key

#employees = [
 #   {"name": "Bhoopathi", "salary": 25000},
  #  {"name": "Rahul", "salary": 18000},
   # {"name": "Priya", "salary": 35000}
#]

#sorted_employees = sorted(
 #   employees,
  #  key=lambda employee: employee["salary"],
   # reverse=True
#)

#print(sorted_employees)

employees = [
    {"name": "Bhoopathi", "salary": 25000},
    {"name": "Rahul", "salary": 18000},
    {"name": "Priya", "salary": 35000},
    {"name": "Kumar", "salary": 45000}
]

medium_salary = list(filter(lambda employee: employee["salary"] >= 25000, employees))
names = list(map(lambda employee: employee["name"], medium_salary))
print(names)