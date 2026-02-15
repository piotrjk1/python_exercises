""" 
- concatenation
- print multiple arguments
- stirng methods: lower, upper, casefold, join
- print termination character
- control characters / escape sequences \n \t \\
"""

print("Hello " + "there")
print("Hello " + str(7))
print("Hello", 100, {1,2,3}, 1.23)

print("Hello".upper())
print("Hello".casefold())
print(",".join({"one", "two", "three"}))
print("Hello", end="....")
print()
print("Hi")

print("Hi, \nhow are \tyou\\")
print('"Hi"')
print("'Hi'")
print("Hello \"Bob\"")