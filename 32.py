list1 = [23,2354456,6,5,68,5,23,11,10]
list2 = [100,2000,1000,10]

list1.append(-1)
list1.append(-10)
print(list1)

list2.insert(2,-4)
list2.insert(2,-10)
print(list2)

list1.extend(list2)

print(list1)
