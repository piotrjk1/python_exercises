import math

def calculate_pi():
    value = 1
    sum = 0.0
    sign = 1

    for i in range(0, 100000):
        sum += sign * 1/value
        value += 2
        sign *= -1

    pi = 4 * sum

    # assert pi > 2.5 and pi < 3.5, f"Pi is out of range {pi}"
    assert abs(pi - math.pi) < 0.0001

  

    return pi

def main():
    approximated_pi = calculate_pi()

    print(approximated_pi)
    print(math.pi)

    difference = math.pi - approximated_pi
    print(f"difference: {difference}")

main()