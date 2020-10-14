import random;

numbers = []

for i in range(10):
    numbers.append(random.randint(-100,100))

totalNumberOfEven = 0
totalNumberOfOdd = 0

print(numbers)

for number in numbers:
    if number % 2 == 0:
        totalNumberOfEven += 1
    else:
        totalNumberOfOdd += 1


print("Total number of even:",totalNumberOfEven)
print("Total number of odd:",totalNumberOfOdd)