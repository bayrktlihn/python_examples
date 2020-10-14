import random;

length = random.randint(-10, 100)
width = random.randint(-10, 100)
height = random.randint(-10, 100)

print("length width height")
print(length,width,height)

volumeOfRectangularPrism = None
if length > 0 and width > 0 and height > 0:
    volumeOfRectangularPrism = length * width * height

if volumeOfRectangularPrism:
    print(volumeOfRectangularPrism)
else:
    print("Invalid someone of given numbers")