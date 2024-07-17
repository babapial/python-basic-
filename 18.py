#nested if else 

a = int(input("enter a "))
b = int(input("enter b "))
c = int(input("enter c "))

if( a>b ) :
    if( a>c ):
        print("a is maximum")
    else :
        print("c is maximum")
        
elif( c>b ) :
    if( a<c ):
        print("c is maximum")
    else :
        print("b is maximum")

elif(b>c):
    if( b>a ):
        print("b is maximum")
    else :
        print("a is maximum")

else:
    print("all equal")