# Factorial

def calculate_factorial(number):
    product = 1
    while number > 0:
        product = product * number
        number = number - 1
    return product
    
print(calculate_factorial(5))

def calculate_factorial_2(number):
    if number <= 1:
        return 1
    return number * calculate_factorial_2(number-1)

print(calculate_factorial_2(5))