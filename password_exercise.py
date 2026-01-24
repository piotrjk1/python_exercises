PASSWORD = "pass1234"

for _ in range(3):
    password = input("Enter your password: ")

    if password == PASSWORD:
        print("Greetings Professor Falcon")
        break

    print("Access denied")

print("Program finished")