numbers = {x for x in range(15)}

numbers.remove(6)
print(numbers)

# numbers.remove(20)

numbers.discard(20) 
# discard próbuje usunąć ale bez errora jeśli nie istnieje

numbers.discard(2)
print(numbers)

# Do not rely on the order of numbers in sets
for x in numbers:
    print(x)
