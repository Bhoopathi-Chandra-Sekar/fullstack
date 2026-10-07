#class Employee:
 #   def show_details(self):
  #      print("Employee details")

#class Developer(Employee):
 #   def show_language(self):
  #      print("Python")

#developer1 = Developer()
#developer1.show_details()
#developer1.show_language()

#class Employee:
 #   def __init__(self, name, salary):
  #      self.name = name
   #     self.salary = salary

#class Developer(Employee):
 #   def __init__(self, name, salary, language):
  #      super().__init__(name, salary)
   #     self.language = language

#developer1 = Developer("Bhoopathi", 40000, "Python")

#print(developer1.name)
#print(developer1.salary)
#print(developer1.language)

#class Employee:
 #   def show_role(self):
  #      print("Employee")

#class Developer(Employee):
 #   def show_role(self):
  #      print("Developer")

#developer1 = Developer()
#developer1.show_role()

#isinstance() - lets us check whether an object belongs to a particular class.

#class Employee:
 #   def __init__(self, name, salary):
  #      self.name = name
   #     self.salary = salary

#class Developer(Employee):
 #   def __init__(self, name, salary, language):
  #      super().__init__(name, salary)
   #     self.language = language

#class Manager(Employee):
 #   def __init__(self, name, salary, team_size):
  #      super().__init__(name, salary)
   #     self.team_size = team_size

#manager1 = Manager("Rahul", 50000, 8)
#print(manager1.name)
#print(manager1.salary)
#print(manager1.team_size)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    def show_role(self):
        print("Developer")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    def show_role(self):
        print("Manager")

developer1 = Developer("Bhoopathi", 40000, "Python")
manager1 = Manager("Rahul", 50000, 8)

developer1.show_role()
manager1.show_role()