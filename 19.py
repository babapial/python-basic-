num = int(input("enter a number"))

if(num%3==0 or num%5==0):
    if(num%15!=0):
        print("YES")
    else :
        print("NO")