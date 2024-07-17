tuples = (1,2,3,4,5,6,7,8,9,10)

print("previous tuple")
print(tuples)

print("recent tuple")
list1 = []
for i in reversed (tuples):
    list1.append(i)

output_tuple = tuple(list1)
 
print(output_tuple)
print(list1)

# list2 = [1,2,3,4,5,6,7,8,9,10]

# for i in reversed (list2):
#     print(i)