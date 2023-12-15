print("Welcome to the python fundamental topic game!")

gameplay = input("Do you want play? ")

if gameplay != "yes":
  print("Ok, maybe next time :( !")
else:
  print("Ok, LET'S PLAY :) !")
Grade = int(0)

answer = input("Are lists mutable in python? ")
if answer == "yes":
  print("CORRECT!")
  Grade = Grade + 10
else:
  print("wrong")

answer = input("Can a variable name have underscores? ")
if answer == "yes":
  print("CORRECT!")
  Grade = Grade + 10
else:
  print("wrong")

answer = input("Are tuples immutable in python? ")
if answer == "yes":
  print("CORRECT!")
  Grade = Grade + 10
else:
  print("wrong")

answer = input("Do floats have decimal points? ")
if answer == "yes":
  print("CORRECT!")
  Grade = Grade + 10
else:
  print("wrong")

answer = input("Does the break statement enable continuation past the for loop body? ")
if answer == "yes":
  print("CORRECT!")
  Grade = Grade + 10
else:
  print("wrong")

answer = input("Is a string a sequence of characters? ")
if answer == "yes":
  print("CORRECT!")
  Grade = Grade + 10
else:
  print("wrong")

answer = input("Is a substring a subset of a string? ")
if answer == "yes":
  print("CORRECT!")
  Grade = Grade + 10
else:
  print("wrong")

answer = input("Are data structures different ways to organize and store data? ")
if answer == "yes":
  print("CORRECT!")
  Grade = Grade + 10
else:
  print("wrong")

answer = input("Is a list a data type? ")
if answer == "yes":
  print("CORRECT!")
  Grade = Grade + 10
else:
  print("wrong")

answer = input("is a dictionary an ordered collection of key-value pairs? ")
if answer == "yes":
  print("CORRECT!")
  Grade = Grade + 10
else:
  print("wrong")

print("You got " + str(Grade) + " out of 100")
print("You got " + str(Grade/10) + " out of 10")