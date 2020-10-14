import random

num = random.randint(-25, 100)

print("Given number is", num)

if num > 0:
    total = (num * (num + 1)) // 2
    print("Total:", total)
else:
    print("Invalid value of number")
