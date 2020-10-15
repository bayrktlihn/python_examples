import random

myList = []

for i in range(0,30):
    myList.append(random.randint(1,100))

print(myList)

myList.sort()
myList.reverse()
print(myList[0:3])