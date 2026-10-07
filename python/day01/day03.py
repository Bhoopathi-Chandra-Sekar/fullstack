#def employee_info(name, salary):
    #print("Name:", name)
    #print("Salary:", salary)

    #if salary >= 30000:
        #print("category: High Salary")
    #elif salary >= 20000:
        #print("category: Medium Salary")
    #else:
        #print("category: Low Salary")

#employee_info("Bhoopathi", 25000)

#def check_result(name, mark):
    #print("Name:", name)
    #print("Mark:", mark)

    #if mark >= 90:
        #print("Result: Excellent")
    #elif mark >= 75:
        #print("Result: Very Good")
    #elif mark >= 50:
        #print("Result: Pass")

    #else:
        #print("Result: Fail")

#check_result("Bhoopathi", 82)

#def show_numbers(start, end):
    #for number in range(start, end):
        #print(number)

#show_numbers(1, 11)

#def show_adults(names, ages):
 #   for i in range(len(names)):
  #      if ages[i] >= 18:
   #         print(names[i])

#names = ["Bhoopathi", "Rahul", "Priya", "Kumar"]
#ages = [24, 17, 22, 16]

#show_adults(names, ages)

def employee_check(name, salary):
    print("Name:", name)
    print("Salary:", salary)

    if salary >= 30000:
        print("category: High Salary")
    elif salary >= 20000:
        print("category: Medium Salary")
    else:
        print("category: Low Salary")

employees = [["Bhoopathi", 25000], ["Rahul", 18000], ["Priya", 35000]]

for employee in employees:
    employee_check(employee[0], employee[1])