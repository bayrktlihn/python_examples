
def isfloat(val):
    tmpVal = val
    if val[0] == "-":
        tmpVal = val[1:]
    return tmpVal.replace(".","",1).isdigit()
def isInt(val):
    tmpVal = val
    if val[0] == "-":
        tmpVal = val[1:]
    return tmpVal.isdigit()

def clearAfterDot(afterDot):
    tmp = afterDot[::-1]
    tmp = str(int(tmp))
    tmp = tmp[::-1]
    if tmp == "0":
        tmp = ""
    return tmp


number = input("Give a number: ")

total = None
if isInt(number):
    total = 0
elif isfloat(number):
    afterDot = number.split(".")[1]
    afterDot = clearAfterDot(afterDot)
    total = len(afterDot)

if total != None:
    print(total)
else:
    print("Invalid value")