#import csv

#with open("employees.csv", "r") as file:
 #   employees = csv.reader(file)

  #  next(employees)         #It takes the next row from the csv reader

   # for employee in employees:
    #    print(employee[0], employee[2])

#import csv

#with open("employees.csv", "r") as file:
 #   employees = csv.reader(file)

  #  next(employees)

   # for employee in employees:
    #    salary = int(employee[2])       #converts the csv salary from a string into an integer

     #   if salary >= 20000:
      #      print("Name:", employee[0])
       #     print("Salary:", salary)

#csv.DictReader
#Python uses the first row of the csv as column names

#import csv

#with open("employees.csv", "r") as file:
 #   employees = csv.DictReader(file)        #Even with DictReader, CSV values are still strings

  #  for employee in employees:
   #     salary = int(employee["salary"])

    #    if salary >= 30000:
     #       print("Name:", employee["name"])
      #      print("Age:", employee["age"])
       #     print("Salary:", salary)

#writing to a csv file

#import csv

#with open("employees.csv", "r") as input_file:
 #   employees = csv.DictReader(input_file)

  #  with open("high_salary_employees.csv", "w", newline="") as output_file:
   #     writer = csv.writer(output_file)

    #    writer.writerow(["name", "age", "salary"])

     #   for employee in employees:
      #      salary = int(employee["salary"])

       #     if salary >= 30000:
        #        writer.writerow([
         #           employee["name"],
          #          employee["age"],
           #         salary
            #    ])

import csv

with open("employees.csv", "r") as input_file:
    employees = csv.DictReader(input_file)

    with open("adult_employees.csv", "w", newline="") as output_file:
        writer = csv.writer(output_file)

        writer.writerow(["name", "age", "salary"])

        for employee in employees:
            age = int(employee["age"])
            salary = int(employee["salary"])

            if age >= 18 and salary >= 20000:
                writer.writerow([
                    employee["name"],
                    age,
                    salary
                ])