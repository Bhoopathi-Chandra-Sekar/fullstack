#Class - class gives us a way to create a reusable structure for employee

#A class is like a blueprint and an object is something we create from that blueprint

#class Employee:
 #   pass        #temporarily means nothing here yet

#employee1 = Employee()

#print(employee1)

#class Employee:
 #   def __init__(self, name, age, salary):
  #      self.name = name
   #     self.age = age
    #    self.salary = salary

#employee1 = Employee("Bhoopathi", 24, 25000)    #object
#employee2 = Employee("Rahul", 17, 18000)        #object

#print(employee2.name)
#print(employee2.salary)

#Methods

#A method is a function that belongs to a class

#class Employee:
    #def __init__(self, name, age, salary):
       # self.name = name
      #  self.age = age
     #   self.salary = salary

    #def show_info(self):
       # print("Name:", self.name)
      #  print("Age:", self.age)
     #   print("Salary:", self.salary)

    #def salary_category(self):
      #  if self.salary >= 30000:
     #       print("High Salary")
    #    elif self.salary >= 20000:
   #         print("Medium Salary")
  #      else:
 #           print("Low Salary")

#employee1 = Employee("Bhoopathi", 24, 25000)
#employee2 = Employee("Priya", 22, 35000)

#employee2.salary_category()

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)

    def salary_category(self):
        if self.salary >= 30000:
            return "High Salary"
        elif self.salary >= 20000:
            return "Medium Salary"
        else:
            return "Low Salary"

    def is_adult(self):
        if self.age >= 18:
            return "Adult"
        else:
            return "Minor"

    def show_status(self):
        print("Name:", self.name)
        print("Salary Category:", self.salary_category())
        print("Status:", self.is_adult())

employee1 = Employee("Bhoopathi", 24, 25000)
employee2 = Employee("Rahul", 17, 18000)
employee3 = Employee("Priya", 22, 35000)

employee1.show_status()
employee2.show_status()
employee3.show_status()


#Classes - blueprint for objects
#Objects - Instances of a class
#__init__() - Initializes object data
#self - refers to the current object
#Attributes - name, age, salary
#Methods - functions inside a class
#return - sends a value back from a method
#conditions inside methods
#creating multiple objects from one class