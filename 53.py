def powerab(a,b):
    multi = 1
    if(b==1):
        return a
    multi = a*powerab(a,b-1)
    return multi

a = int(input("enter a : "))
b = int(input("enter b : "))

ans = powerab(a,b)
print("result of a^b is = ",ans)