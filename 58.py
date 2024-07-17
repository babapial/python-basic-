def palindrome(s):
    temp =  s[::-1]
    if(temp==s):return 1
    else :return 0
    
        

s = input("enter the sring   ")
ans = palindrome(s)
if(ans==1):
    print("palindrome")
else :
    print("not palindrome")