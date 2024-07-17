def fact(n):
    if n==1 or n==0:
        return 1
    ans = n*fact(n-1)
    return ans
    
    
n = int(input("enter n   :  "))

ans = fact(n)
print("ans is ",ans)