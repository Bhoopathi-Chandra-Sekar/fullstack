#def add_numbers(*args):
 #   print(args)

#add_numbers(10, 20, 30, 40)

#def add_numbers(*args):
 #   for number in args:
  #      print(number)

#add_numbers(10, 20, 30, 40)

#def calculate_total(*args):
 #   total = 0

  #  for number in args:
   #     total = total + number

    #return total

#result = calculate_total(10, 20, 30, 40, 50)
#print(result)

#*args doesn't have to be named args. The * is what matters:

#def calculate_total(*numbers):      #Here number is still a tuples containing all the arguments 
 #   total = 0

  #  for number in numbers:
   #     total = total + number

    #return total

#result = calculate_total(10, 20, 30, 40, 50)
#print(result)

#**Kwargs

#*args collects multiple positional arguments.             args = tuple
#**kwargs collects multiple named/keyword arguments.       kwargs = dictionary

#Example:

#def employee_info(**details):       #**kwargs collects the values as dictionary.
 #   print(details)

#employee_info(name = "Bhoopathi", age = 24, salary = 25000)

#def show_employee(**details):
 #   print("Name:", details["name"])
  #  print("Age:", details["age"])
   # print("Salary:", details["salary"])

#show_employee(name = "Bhoopathi", age = 24, salary = 25000)

#def employee_summary(*skills, **details):
 #   print("Name:", details["name"])
  #  print("Age:", details["age"])
   # print("Salary:", details["salary"])
    #print("Skills:", skills)

#employee_summary(
 #   "Python",
  #  "HTML",
   # "CSS",
    #name = "Bhoopathi",
    #age = 24,
    #salary = 25000
#)

#def show_employee(*skills, **details):
 #   print("Name:", details["name"])
  #  print("Salary:", details["salary"])
   # print("Skills:", skills)

    #if "Python" in skills:
     #   print("Python Developer")

    #else:
     #   print("Other Developer")


#show_employee(
 #   "Python",
  #  "HTML",
   # "CSS",
    #name = "Bhoopathi",
    #salary = 25000
#)

def employee_summary(*skills, **details):
    print("Name:", details["name"])
    print("Number of Skills:", len(skills))
    print("Skills:", skills)
    print("Salary:", details["salary"])

    if details["salary"] >= 30000:
        print("High Salary")
    else:
        print("Normal Salary")

employee_summary(
    "Python",
    "HTML",
    "CSS",
    "JavaScript",
    name = "Bhoopathi",
    salary = 25000
)