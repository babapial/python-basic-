def printn(n):
    
    if n==0:
        return 
    
    #print(n)
    
    
    printn(n-1)
    print(n)
    


n =int(input("enter n  :  "))
printn(n)