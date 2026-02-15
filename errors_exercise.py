def convert_feet_to_miles(feet):
    miles = feet * 1.89E-4
    print("Distance in miles: %.3f" % (miles))

def main():
    feet = input("Enter a distance in feet: ")
    while(feet != "quit"):
        try:
            convert_feet_to_miles(float(feet))
            feet = "quit"
        except ValueError:
            print("Błąd. Podana wartość musi być liczbą!")
            feet = input("Enter a distance in feet: ")

main()