dic = {}

n = int(input("enter the number"))
for _ in range(n):
    key = (input("enter the key"))
    value = int(input("enter values"))
    dic[key] = value

sum = 0 

for i in dic:
    sum +=dic[i]

print("total sum is =  ",sum)

# 4
# pial
# 100
# mim
# 200
# piyas
# 50
# adip
# 200

print("sum ",sum(dic.values()))