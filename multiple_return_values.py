def get_user_info():
    name = input("Enter your name > ")
    height = input("Enter your height > ")

    return name, height


def get_user_info_2():
    weight = float(input("Enter your weight in kilos > "))
    height = float(input("Enter your height in metres > "))
    bmi = weight / (height * height)

    return weight, height, bmi

def main():
    name, height = get_user_info()
    print(name + ": " + height)

    weight, height, bmi = get_user_info_2()
    print("Weight:",weight,"Height:",height,"BMI:",bmi)

main()