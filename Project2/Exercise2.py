# Scientific Calculator Without Libraries

PI = 3.141592653589793


# Square Root using Newton's Method
def square_root(x):
    if x == 0:
        return 0

    guess = x

    for i in range(100):
        guess = (guess + x / guess) / 2

    return guess


# Convert Degrees to Radians
def to_radians(angle):
    return angle * PI / 180


# Sine using Taylor Series
def sine(angle):
    x = to_radians(angle)

    while x > PI:
        x -= 2 * PI

    while x < -PI:
        x += 2 * PI

    result = 0
    term = x

    for i in range(12):
        result += term
        term = -term * x * x / ((2 * i + 2) * (2 * i + 3))

    return result


# Cosine using Taylor Series
def cosine(angle):
    x = to_radians(angle)

    while x > PI:
        x -= 2 * PI

    while x < -PI:
        x += 2 * PI

    result = 0
    term = 1

    for i in range(12):
        result += term
        term = -term * x * x / ((2 * i + 1) * (2 * i + 2))

    return result


# Natural Logarithm using a Series
def natural_log(x):
    if x <= 0:
        return None

    count = 0

    while x >= 2:
        x /= 2
        count += 1

    while x < 1:
        x *= 2
        count -= 1

    z = (x - 1) / (x + 1)
    result = 0
    power = z

    for i in range(100):
        result += power / (2 * i + 1)
        power *= z * z

    ln_x = 2 * result

    # Calculate ln(2)
    z = 1 / 3
    power = z
    ln_2 = 0

    for i in range(100):
        ln_2 += power / (2 * i + 1)
        power *= z * z

    ln_2 *= 2

    return ln_x + count * ln_2


# Floor Function
def floor_number(x):
    result = int(x)

    if x < result:
        result -= 1

    return result


# Ceiling Function
def ceiling_number(x):
    result = int(x)

    if x > result:
        result += 1

    return result


while True:

    print("\n===== Scientific Calculator =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Square Root")
    print("7. Percentage")
    print("8. Sin")
    print("9. Cos")
    print("10. Tan")
    print("11. Log")
    print("12. Natural Log")
    print("13. Factorial")
    print("14. Absolute Value")
    print("15. Floor")
    print("16. Ceiling")
    print("17. Pi")
    print("18. Exit")

    choice = int(input("Choose an operation: "))

    match choice:

        case 1:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a + b)

        case 2:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a - b)

        case 3:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a * b)

        case 4:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if b != 0:
                print("Result:", a / b)
            else:
                print("Cannot divide by zero!")

        case 5:
            a = float(input("Enter base: "))
            b = float(input("Enter power: "))
            print("Result:", a ** b)

        case 6:
            a = float(input("Enter number: "))

            if a >= 0:
                print("Result:", square_root(a))
            else:
                print("Invalid number!")

        case 7:
            a = float(input("Enter number: "))
            b = float(input("Enter percentage: "))
            print("Result:", a * b / 100)

        case 8:
            a = float(input("Enter angle in degrees: "))
            print("Result:", sine(a))

        case 9:
            a = float(input("Enter angle in degrees: "))
            print("Result:", cosine(a))

        case 10:
            a = float(input("Enter angle in degrees: "))
            c = cosine(a)

            if abs(c) > 0.0000000001:
                print("Result:", sine(a) / c)
            else:
                print("Undefined!")

        case 11:
            a = float(input("Enter number: "))

            if a > 0:
                print("Result:", natural_log(a) / natural_log(10))
            else:
                print("Invalid number!")

        case 12:
            a = float(input("Enter number: "))

            if a > 0:
                print("Result:", natural_log(a))
            else:
                print("Invalid number!")

        case 13:
            a = int(input("Enter number: "))

            if a >= 0:
                result = 1

                for i in range(1, a + 1):
                    result *= i

                print("Result:", result)
            else:
                print("Invalid number!")

        case 14:
            a = float(input("Enter number: "))

            if a < 0:
                a = -a

            print("Result:", a)

        case 15:
            a = float(input("Enter number: "))
            print("Result:", floor_number(a))

        case 16:
            a = float(input("Enter number: "))
            print("Result:", ceiling_number(a))

        case 17:
            print("Pi =", PI)

        case 18:
            print("Calculator closed!")
            break

        case _:
            print("Invalid choice!")
    
