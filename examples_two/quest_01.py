import random

def isInteger(val):
    if val.isdigit():
        return True
    elif val[0] == "-" and val[1:].isdigit():
        return True
    return False

randomNumber = random.randint(1, 10)
total = 0

isOver = False

while not isOver:
    givenValue = input("Please give a number: ")


    if isInteger(givenValue):
        givenValue = int(givenValue)

        if givenValue > 0 and givenValue < 11:
            total += 1
            if givenValue > randomNumber:
                print("Enter less than number that you gave the number")
            elif givenValue < randomNumber:
                print("Enter greater than number that you gave the number")
            else:
                isOver = True

        else:
            print("Please give number between 1 and 10")


print("You found it on the",total,"try")




