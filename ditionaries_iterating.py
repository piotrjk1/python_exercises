def main():
    fruits = {
        "apple": "green",
        "orange": "orange",
        "banana": "yellow"
    }

    for fruit in fruits:
        print(fruit + ": " + fruits[fruit])

    print()

    for fruit in fruits.keys():
        print(fruit)

    print()

    for fruit in fruits.values():
        print(fruit)

    print("apple" in fruits)

    for item in fruits.items():
        print(item)

    for item in fruits.items():
        (fruit, color) = item
        print(fruit + ", " + color)

    for fruit, color in fruits.items():
        print(fruit + ", " + color)

main()