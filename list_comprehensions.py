animals1 = ["dog", "goat", "sloth", "tiger"]

""" 
animals2 = animals1

del animals2[1]

print(animals1)
print(animals2)
"""

# animals3 = animals1.copy()
# del animals3[1]
# print(animals1)
# print(animals3)

animals4 = [animal for animal in animals1]
print(animals4)

# animals5 = [10 for animal in animals1]
# print(animals5)

animals6 = [animal.upper() for animal in animals1]
print(animals6)

lengths = [len(text) for text in animals1]
print(lengths)

print()
numbers1 = [3, 6, 3, 8, 5]
numbers2 = [x*x for x in numbers1]
print(numbers2)