#Python has built-in modules that let us interact with  the computer
#os module
#os is commonly used for working with:
#Files
#Folders
#paths
#directories

#import os

#print(os.getcwd())

#import os

#print(os.path.exists("hello.py"))

#import os

#print(os.path.isfile("day14.py"))  #is it a file?
#print(os.path.isdir("day14.py"))   #is it a folder?

#import os

#os.mkdir("employees")
#print("Folder created")

#import os

#if not os.path.exists("employees"):
 #   os.mkdir("employees")
  #  print("Folder created")

#else:
 #   print("Folder already exists")

#import os

#print(os.listdir())

#os.path.join() - this lets python combine folder names and file names

#import os

#file_path = os.path.join("employees", "employee.txt")

#with open(file_path, "w") as file:
 #   file.write("Bhoopathi\nDeveloper")

#print("File created")

#import os

#items = os.listdir()

#for item in items:
 #   if os.path.isdir(item):
  #      print(item)

#import os

#os.rename("employees/employee.txt", "employee.txt")
#print("File moved")

#import os

#if not os.path.exists("text_files"):
 #   os.mkdir("text_files")

#if not os.path.exists("images"):
  #  os.mkdir("images")

#if not os.path.exists("documents"):
 #   os.mkdir("documents")

#print("Folders ready")

#import os

#os.rename("notes.txt", "text_files/notes.txt")

#import os

#os.rename("photo.jpg", "images/photo.jpg")
#print("File moved")

#import os

#os.rename("report.pdf", "documents/report.pdf")
#print("File moved")

#import os

#file_name = "photo.jpg"

#name, extension = os.path.splitext(file_name)

#print(name)
#print(extension)

import os

items = os.listdir()

for item in items:
    if os.path.isfile(item):
        if item == "day14.py":
            continue

        name, extension = os.path.splitext(item)
        print(item, "-", extension)

        if extension == ".txt":
            folder = "text_files"
        elif extension == ".jpg":
            folder = "images"
        elif extension == ".pdf":
            folder = "documents"
        elif extension == ".py":
            folder = "python_files"

        if not os.path.exists(folder):
            os.mkdir(folder)

        destination = os.path.join(folder, item)
        os.rename(item, destination)
        print(item, "moved")

        print(folder)