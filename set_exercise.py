def main():
    x = 1
    cubic = {1}

    while(x*x*x <= 729):
      cubic.add(x*x*x)
      x += 1

    print(cubic)

    y = 1
    square = {1}
    while(y*y <= 729):
       square.add(y*y)
       y += 1
    print(square)


main()
