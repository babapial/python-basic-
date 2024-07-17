list1 = []

n = int(input("enter list number :  "))

ind1 = int(input("enter fisrt index :  "))
ind2 = int(input("enter second index :  "))

for i in range(0,n):
    ele = int(input())
    list1.append(ele)
    
temp = list1[ind1]
list1[ind1] = list1[ind2]
list1[ind2] = temp 
print(list1)