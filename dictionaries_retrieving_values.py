fruits = {
    "apple": "green",
    "orange": "orange",
    "banana": "yellow",
}

# color = fruits["mango"]     error, bo nie ma tego w słowniku
color = fruits.get("mango")

print(color)
print(type(color))

# domyślna wartość, jeśli nie istnieje 
color = fruits.get("mango", "red")
print(color)
print(type(color))