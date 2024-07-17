colour =("red","green","yellow")
print(colour)
print(colour[2])
print(colour[-1])
print(len(colour))
print(type(colour))
print(colour[1:3])

if "green" in colour :
    print("green part of tuple")

for i in colour :
    print(i)
    
more_colours = ("blue","brown","pink")

more_colours = colour+more_colours
print(more_colours)

colour1,colour2,colour3 = colour 
print(colour1,colour2,colour3)
print(type(colour1))