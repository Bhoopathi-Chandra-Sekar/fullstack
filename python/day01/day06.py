#.upper()   #uppercase
#.lower()   #lowercase
#.strip()   #removes extra spaces from beginning and the end
#.replace() #It replace one piece of text with another
#.split()   #It breaks a string into separate pieces and gives you a list 

#text = "Python-HTML-CSS"

#print(text.replace("-", " ").split())

#file = open("message.txt", "r")   #Open

#content = file.read()    #Read

#print(content)     #Print

#file.close()     #Close

#file = open("message.txt", "r")    #read - r

#for line in file:   #Take each line from the file, one at a time.
#    print(line.strip())

#file.close()

#file = open("output.txt", "w")     #write - w

#file.write("I am learning Full Stack Development.")

#file.close()

#file = open("output.txt", "a")    #append - a

#file.write("\nPython is my first programming language.")

#file.close()

#file = open("output.txt", "a")

#file.write("\nI will become a Full Stack Developer")

#file.close()

#try:
 #   number = int(input("Enter a number: "))
  #  print("You entered:", number)

#except:
 #   print("Enter a valid number.")

#try:
 #   number = int(input("Enter a number: "))

  #  if number >= 18:
   #     print("Adult")
    #else:
     #   print("Minor")

#except:
 #   print("Invalid input")


def save_employee(name, salary):
    file = open("employees.txt", "a")

    file.write("Name: " + name + "\n")
    file.write("Salary: " + str(salary) + "\n")
    file.write("----------------\n")

    file.close()

save_employee("Rahul", 18000)
save_employee("Priya", 35000)
