a=input("enter the number to be checked")
temp=a
b=0
while(a!=0):
    c=a%10
    b=b*10+c
    a=a/10
print b
if(b==temp):
    print "the number you entered is palindrome"
else:
    print "the number you entered is not a palindrome number"
                                                                            
