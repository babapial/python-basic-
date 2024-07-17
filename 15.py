eng = int(input("enter the english marks"))
mat = int(input("enter the math marks"))

if (eng>80 and mat>80):
    print("A+")
elif(eng>80 or mat>80):
    print("A")
else :
    print("PASS")