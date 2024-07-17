s = input("Enter the string: ")
n = int(input("Enter the index: "))
dic = {
    "a" : "z",
    "b" : "y",
    "c": "x",
    "d" : "w",
    "e" : "v",
    "f" : "u",
    "g" : "t",
    "h" : "s",
    "i" : "r",
    "j" : "q",
    "k" : "p",
    "l" : "o",
    "m" : "n"
}

ans = ""
for index, item in enumerate(s):
    #print(item)
    if index > n - 2:
        if item in dic:
            #print(dic[item])
            print(item)
            ans = ans + dic[item]
    else:
        ans = ans + item
        print(item)
        
print("final ans :",ans)

# s = input("enter the string ")
# n = int(input("enter the index "))
# dic = {
#     "a" : "z",
#     "b" : "y",
#     "c": "x",
#     "d" : "w",
#     "e" : "v",
#     "f" : "u",
#     "g" : "t",
#     "h" : "s",
#     "i" : "r",
#     "j" : "q",
#     "k" : "p",
#     "l" : "o",
#     "m" : "n"
    
# }

# ans = ""
# for i in range(0,len(s)):
    
#     if i>=n-2:
#         ans = ans+(dic[(s[i])])
#         #temp = (chr(dic[(s[i])]))
#         #s[i].replace(temp,temp)
#         #s[i] = chr(temp)
#         #s[i] = chr(temp)
#         #ans.append(temp)
#     # else:
#     #     ans.append(s[i])
        
# print("final ans   ",s)