def fact(n):
    ans = 1
    if n==0 or n==1:
        return ans
    for i in range(1,n+1):
        ans = ans*i
    
    return ans


n = int(input("enter n : "))
ans = fact(n)

print("the factorial of ",n," is :",ans)