
import math

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
                print("Result:", math.sqrt(a))
            else:
                print("Invalid number!")

        case 7:
            a = float(input("Enter number: "))
            b = float(input("Enter percentage: "))
            print("Result:", a * b / 100)

        case 8:
            a = float(input("Enter angle in degrees: "))
            print("Result:", math.sin(math.radians(a)))

        case 9:
            a = float(input("Enter angle in degrees: "))
            print("Result:", math.cos(math.radians(a)))

        case 10:
            a = float(input("Enter angle in degrees: "))
            if a % 180 != 90:
                print("Result:", math.tan(math.radians(a)))
            else:
                print("Undefined!")

        case 11:
            a = float(input("Enter number: "))
            if a > 0:
                print("Result:", math.log10(a))
            else:
                print("Invalid number!")

        case 12:
            a = float(input("Enter number: "))
            if a > 0:
                print("Result:", math.log(a))
            else:
                print("Invalid number!")

        case 13:
            a = int(input("Enter number: "))
            if a >= 0:
                print("Result:", math.factorial(a))
            else:
                print("Invalid number!")

        case 14:
            a = float(input("Enter number: "))
            print("Result:", abs(a))

        case 15:
            a = float(input("Enter number: "))
            print("Result:", math.floor(a))

        case 16:
            a = float(input("Enter number: "))
            print("Result:", math.ceil(a))

        case 17:
            print("Pi =", math.pi)

        case 18:
            print("Calculator closed!")
            break

        case _:
            print("Invalid choice!")

