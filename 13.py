cost = int(input("enter cost price"))
sell = int(input("enter sell price"))

if cost == sell :
    print("no loss not proift")
elif cost>sell :
    print("loss")
    print("loss amount is ",cost-sell)
else :
    print("profit") 
    print("profit amount is ",sell-cost)