def do_greet():
    d = dict()
    # print(d["hello"])
    greet()

def greet():
    print("Hello")
    print(1/0)

def main():
    try:
        do_greet()
    except ZeroDivisionError:
        print("Treid to divied by zero!")
    except KeyError:
        print("A key error occured")
    except:
        print("Some unknown error occured")

main()