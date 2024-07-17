def total_sum(n):
    sum = 0 
    if n==0:
        return 0
    sum = n+total_sum(n-1)
    return sum



n = int(input("enter the number"))
ans = total_sum(n)
print("total sum is : ",ans)