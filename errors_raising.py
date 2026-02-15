def do_greet():
    # raise KeyError("Not a real key error!")
    raise Exception("Not a real error")
    greet()

def greet():
    print("Hello")
    print(1/0)

def main():
    try:
        do_greet()
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
    except KeyError as ke:
        print(f"Key Error: {ke}")
    except Exception as e:
        print(f"General error: {e}")
main()