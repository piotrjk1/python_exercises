WORKER1 = "John"
WORKER2 = "Rachel"
PROFESSOR = "Falcon"

name = input("Enter your name: ")

if name == WORKER1:
    print("Hello John!")
elif name == WORKER2:
    print("Ciao Rachel!")
elif name == PROFESSOR:
    print("Good morning Falcon!")
else:
    print("Name not recognised.")

print("Program finished")
