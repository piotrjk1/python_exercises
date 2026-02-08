def main():
    people = ["Amelia", "Arthur", "Isla", "Noah", "Ava", "Leo", "Mia", "Oscar"]
    ages = [20, 30, 25, 65, 21, 70, 32, 45]

    dictionary = dict()

    for x in range(len(people)):
        dictionary.update({people[x]:ages[x]})
    print(dictionary)

    exit = False
    while not exit:
        option = input("Jeśli chcesz zakończyć wpisz `quit` w innym razie wciśnij Enter ")
        if option == "quit":
            exit = True
        
        



main()