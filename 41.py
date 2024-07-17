sets = [100,99,98,1,2,3,4,5,6,7,8,9,10]

print(sets)
for i in sets:
    print(i,end=" ")

print(("\n"))
for i in reversed(sets):
    print(i,end=" ")

print(("\n"))
print(sets[0])

sets1 = {"sia","mia","tia","mim","piyas"}
print(sets1)  #not indexing

print(len(sets1))
print(type(sets1))

if "sia" in sets1 :
    print("sia is a part of sets")
    
sets1.add("parvin")
print(sets1)
sets1.add("mim")
print(sets1)
name_list = ["adip","ariha"]
sets1.update(name_list)
print(sets1)
sets1.remove("mia")
print(sets1)

s1 = {'a','b','c'}
s2 = {'e','f','a'}

# s1 = s1.union(s2)
# print(s1)

s1.intersection_update(s2)
print(s1)

s1.symmetric_difference_update(s2)
print(s1)
