""" 
Clock
5 + 12 = 5
"""

def ktora_godzina(godzina, uplyw_godzin):
    nowa_godzina = (godzina + uplyw_godzin)%12
    print(nowa_godzina)

def main():
    ktora_godzina(5,3)

    print()

    for i in range(0, 30):
        print(i % 12, end=" ")

    animals = ["dog", "cat", "cow"]

    for i in range(0, 30):
        animal = animals[i % len(animals)]
        print(animal, end=", ")    


main()