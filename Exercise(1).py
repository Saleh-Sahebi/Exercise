
# If
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Child")


# For
width = int(input("Enter width: "))
height = int(input("Enter height: "))

for i in range(height):
    for j in range(width):
        print("*", end=" ")
    print()


# While
while True:
    print("Project is running")

    stop = input("Type stop to exit: ")

    if stop == "stop":
        break

