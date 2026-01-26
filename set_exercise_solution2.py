def main():
    cubic_set = {x*x*x for x in range(10)}
    print(cubic_set)


    square_set = {x*x for x in range(28)}
    print(square_set)

    print(cubic_set.intersection(square_set))
    print(cubic_set.difference(square_set))


main()