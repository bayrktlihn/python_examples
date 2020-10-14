totalOrderPrice = float(input("Give a total order price: "))
tipAmount = input("Give a tip(%5, %10, %15 ): ")

allowedTipAmount = [0.05, 0.1, 0.15]

if tipAmount[0] == "%":
    tipAmount = tipAmount[1:]
if tipAmount.replace(".", "", 1).isdigit():
    tipAmount = float(tipAmount) / 100
else:
    tipAmount = None



if tipAmount != None and tipAmount in allowedTipAmount:
    totalTip = totalOrderPrice * tipAmount
    print("Total tip:",totalTip)
    totalPrice = totalOrderPrice + totalTip
    print("Total Price:",totalPrice)
else:
    print("Invalid value of tip")