def isIntAndPositive(val):
    if val.isdigit():
        return True

number = input("Please a give number: ")


if isIntAndPositive(number):
    number = int(number)

    total = 0
    for i in range(0, 3):
        total += number * int("1" * (i + 1))

    print(total)

else:
    print("Invalid value")
