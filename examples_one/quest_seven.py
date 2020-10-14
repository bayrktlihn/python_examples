import random;

ageOfHuman = random.randint(-25, 100)

print("Selected:",ageOfHuman)

if ageOfHuman > 0:
    ageOfDog = 0

    if ageOfHuman < 14:
        ageOfDog = ageOfHuman / 7
    elif ageOfHuman < 21:
        ageOfDog = (ageOfHuman / 10.5)
    else:
        ageOfDog += 2
        ageOfHuman -= 21
        ageOfDog += (ageOfHuman / 4)

    print("Age of dog:", ageOfDog)
else:
    print("Invalid age of human")
