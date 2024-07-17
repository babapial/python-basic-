#logical operator


exp1 = 2>1
exp2 = 5<4

print("exp1 and exp2" , exp1 and exp2)
print("exp1 or exp2" , exp1 or exp2)
print("exp2 not" , not (exp2))


#idetity operator

name1 = "pial hasan"
name2 = "pial khan"
name3 = "pial hasan"
print(name1 is name2)
print(name1 is name3)
print(name1 is not name2)


#membership operator 

fruit = ["apple","mango","banana"]
print("pial" in fruit)
print("pial" not in fruit) 

#bitwise operator 

a = 5
b = 3

print(" a and b : ",a&b)
print(" a or b : ",a|b)
print(" a xor b : ",a^b)
print(" a not ",~a)
print("a left shift ",a<<1)
print("a right shift ",a>>1)
 