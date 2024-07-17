text = "PP is always play football in the filed on pp side "
print("string is ",text)
print("string lenght is  ",len(text))

val = (text.find("pp"))
print(val)
if(val>=0):
    print("pp is the part of the stirng ")
else:
    print("pp is not the part of the string ")
    
print("the 0 to 10 th index substring is ",text[0:11])
print(text.replace("always","never"))

new = "no matter what"
print("new string is ",text+new)
