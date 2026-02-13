def main():
    numbers = [[1,2,3], [4,5,6], [7,8], [9, 'A', 'B', 'C']]

    sublist = numbers[1]
    print(sublist)

    print(sublist[2])

    print(numbers[2][1])

    for li in numbers:
        for number in li:
            print(number, end=" ")
        print()


    for i in range(0, len(numbers)):
        for j in range(0, len(numbers[i])):
            print(numbers[i][j], end=" ")
        print()



main()