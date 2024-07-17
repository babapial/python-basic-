n = int(input("enter number : "))

for i in range(0,n+1):
    c = 65
    for j in range(0,i+1):
        char = chr(c+j)
        print(char,end=" ")
    print(" ")        