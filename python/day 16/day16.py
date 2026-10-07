class Employee:
    def __init__(self, name, salary, job):
        self.name = name
        self.salary = salary
        self.job = job

    def show_details(self):                 #self refers to the object that is currently calling the method (funtion that belongs to an object)
        print(self.name, "is a", self.job, "and earns", self.salary)

    def give_raise(self, amount):
        #self.salary = self.salary + amount
        self.salary += amount

employee1 = Employee("Bhoopathi", 30000, "Developer")        #object 1
employee2 = Employee("Rahul", 18000, "Tester")               #object 2

employee1.salary = 35000
employee1.give_raise(5000)

print(employee1.name)
print(employee1.salary)
print(employee2.name)
print(employee2.salary)

employee1.show_details()
employee2.show_details()