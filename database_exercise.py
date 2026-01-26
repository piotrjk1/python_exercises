def show_menu(menu):
    print(menu)

def show_database(db):
    for x in range(len(db)):
        print(str(x) + ": " + db[x])

def add_item(db):
    new_item = input("Enter a new item to the list: ")
    db.append(new_item)

def change_item(db):
    change_index = int(input("Enter the list number of an item to change: "))
    change_item = input("Enter a new value: ")
    db[change_index] = change_item

def delete_item(db):
    del_index = int(input("Enter the list number of an item to delete: "))
    del db[del_index]

def main():
    MENU = """
    1. Display database
    2. Add an item
    3. Delete an item
    4. Change an item
    5. Quit
    """
    option = 0
    lista = ["orange", "banana", "blackberry"]
    
    while not option == 5:
        show_menu(MENU)
        option = int(input("> "))

        if option == 1:
            show_database(lista)

        elif option == 2:
            add_item(lista)

        elif option == 3:
            delete_item(lista)

        elif option == 4:
            change_item(lista)


main()