def isIntAndPositive(val):
    if val.isdigit():
        return True

number = input("Please a give number: ")


if isIntAndPositive(number):
    number = int(number)

    x = "1"
    total = 0
    for i in range(0, 3):
        total += number * int(x)
        x = str(x) + "1"
    print(total)

else:
    print("Invalid value")
