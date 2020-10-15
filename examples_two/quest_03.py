def isNumeric(val):
    if val.isdigit():
        return True
    elif val[0] == "-" and val[1:].isdigit():
        return True

    tmp = val + ""
    if tmp[0] == "-":
        tmp = tmp[1]

    if tmp.replace(".","", 1).isdigit():
        return True
    return False

number = input("Please a give number: ")

if isNumeric(number):
    number = float(number)

    total = 0
    for i in range(0, 3):
        total += number ** (i + 1)
    print(total)

else:
    print("Invalid value")





