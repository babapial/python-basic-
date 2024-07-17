def addone(x):
    x = x+1
    print("inside function ",x)
    
x = 5
addone(x)
print("outside fuction ",x)

def modifylist(lst):
    lst.append(10)
    print("inside fuction : ",lst)
    
lst=[1,2,3,50]
modifylist(lst)
print("outside list is ",lst)