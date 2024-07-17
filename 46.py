s = input("enter the string ")
n = int(input("enter the index "))


alpha ="abcdefghijklmnopqrstuvwxyz"
revalpha = alpha[::-1]
# print(alpha)
# print(revalpha)

dict1 = dict(zip(alpha,revalpha))

prefix = s[0:n-1]
suffix = s[n-1:]

ans = ""

for i in range (0,len(suffix)):
    ans+=dict1[suffix[i]]

prefix+=ans
print("ans is ",prefix)