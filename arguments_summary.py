def function_1(name, age=-1, color="none"):
    print(name, age, color)
    print()

def function_2(*args):
    for arg in args:
        print(arg)
    print()

def function_3(**kwargs):
    for keyword in kwargs:
        print(keyword, ": ", kwargs[keyword])
    print()

def single_function(name, *args, **kwargs):
    print(name)
    for arg in args:
        print(arg)
    for kw in kwargs:
        print(kw,":",kwargs[kw])

def main():
    function_1("Piotr", 27, "white")
    function_2("Siema", "Hej", "Witaj")
    function_3(height=181, weight=79, body_fat=16.6)
    single_function("Piotr", "raz", "dwa", height=181, weight=79, body_fat=16.6)

main()