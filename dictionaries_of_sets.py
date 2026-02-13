def find_book(library, book):

    for books in library.values():
        if book in books:
            return True
    return False


def add_book(library, category, title):
    if not category in library:
        library[category] = set()

    library[category].add(title)


def main():

    library = {
        "Science Fiction" : {"Journey to the Centre of the Earth", "Day of the Triffids"},
        "Drama" : {"A Tale of Two Cities", "Moby Dick"},
    }

    add_book(library, "Science Fiction", "The War of the Worlds")

    print(library)

    for category in library:
        books = library[category]
        
        print(category + ": ", end="")
        print(", ".join(books))

    print(find_book(library, "The War of the Worlds"))


main()