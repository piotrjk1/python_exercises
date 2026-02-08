NAME = "Oscar"
name = "oscar"

print(NAME.lower() == name.lower())

# zamiast tego do takich przypadków można użyć casefold()

print(NAME.casefold() == name.casefold())
# bo niemiecka literka B taka z reską to mała ss chyba

names = {"Bob": 45}

age = names.get("Jim")
print(age)

if age is None:
    print("Name not found")

if age == None:
    print("Name not found")