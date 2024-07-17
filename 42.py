set1 = {1,5,10,20,40,80}
set2 = {6,7,20,80,100,1}
set3 = {3,4,15,20,30,70,80,120}

new = set(set1.intersection(set2))
print(new)
new = set(set3.intersection(new))
print("final  ",new)