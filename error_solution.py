# import re

def feet_to_miles(feet):
    return feet * 1.89E-4

def main():

    while True:
        feet = input("Enter distance in feet > ")

        if feet == "quit":
            break

        try:
            # feet = re.sub(",", "", feet)
            feet = feet.replace(",", "")
            miles = feet_to_miles(float(feet))
            print(f"{feet} is equivalent to {miles:.3f}")
            break
        except:
            print("Invalid input")

main()