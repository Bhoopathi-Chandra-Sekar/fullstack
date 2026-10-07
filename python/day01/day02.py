# =========================
# DAY 2 - LOOPS, LISTS & FUNCTIONS
# =========================


# 1. WHILE LOOP

count = 1

while count <= 5:
    print(count)
    count = count + 1


# 2. FOR LOOP

for number in range(1, 6):
    print(number)


# 3. EVEN NUMBERS

for number in range(1, 11):
    if number % 2 == 0:
        print(number)


# 4. LIST

names = ["Bhoopathi", "Rahul", "Kumar", "Suresh", "Priya", "Vijay"]

print(names)


# 5. LIST INDEX

print(names[0])
print(names[1])


# 6. CHANGE A LIST ITEM

names[1] = "Arun"

print(names)


# 7. APPEND

names.append("Suresh")

print(names)


# 8. LOOP THROUGH A LIST

for name in names:
    print(name)


# 9. REMOVE

names.remove("Kumar")

print(names)


# 10. POP

names.pop(0)

print(names)


# 11. INSERT

names.insert(1, "Priya")

print(names)


# 12. LEN

print(len(names))


# 13. FILTER USING IF

for name in names:
    if name != "Priya":
        print(name)


# 14. FUNCTION

def welcome():
    print("Welcome to Python!")


welcome()


# 15. FUNCTION WITH PARAMETER

def greet(name):
    print("Hello", name)


greet("Bhoopathi")


# 16. FUNCTION WITH RETURN

def multiply(a, b):
    return a * b


result = multiply(5, 4)
print(result)


# 17. FUNCTION + LIST

def print_names(names):
    for name in names:
        print(name)


names = ["Bhoopathi", "Rahul", "Priya"]

print_names(names)


# 18. DAY 2 MINI PROJECT

def show_names(names):
    for name in names:
        print(name)

    print("There are", len(names), "names")


names = ["Bhoopathi", "Rahul", "Kumar", "Suresh", "Priya"]

show_names(names)