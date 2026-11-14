while True:

    number = int(input("Enter a number (0 to exit): "))

    if number == 0:
        print("Program finished!")
        break

    elif number > 0:

        if number % 2 == 0:
            print("This is an even number")

        else:
            print("This is an odd number")

        print("Counting:")

        for i in range(1, number + 1):
            print(i)

    else:
        print("Please enter a positive number!")
        
