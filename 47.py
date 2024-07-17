# n = int(input("enter the number"))

# sum = 0 

# for i in range(1,n+1):
#     sum+=i

# print("total sum is =  ",sum)

def sum(n):
    ans = 0 
    for i in range(1,n+1):
        ans+=i
    return ans

n = int(input("enter the number"))

print("total sum is ",sum(n))   #positoanl arguments


def add_two_number(a,b):
    ans = a+b
    print("a is ",a ," b is ",b)
    return ans
print("two values sum is ",add_two_number(a = 10,b = -5)) #name or keyword arguments


def add_three_number(a,b,c = 0):
    ans = a+b+c
    return ans        

print("three values sum is ",add_two_number(a = 10,b = -5,)) #default arguments


def add_all_number(*args):
    sum = 0 
    for i in args:
        sum+=i
    return sum

print("all number sum is  ",add_all_number(1,2,3,-3,5))  # arbitary arguments

def studet_info(**kwag):
    for x,y in kwag.items():
        print(x,"  is  ",y)
        
studet_info(name = "pial", age = 20 , city = "dhaka")
studet_info(name = "mim", age = 12 , city = "khulna")
studet_info(name = "adip", age = 25 , city = "dhaka")