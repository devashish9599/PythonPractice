a=int(input("enter the number to be checked"))
temp=a
b=0
while(a!=0):
 c=a%10
 b=b*10+c
 a=a/10
if(b==temp):
 print "number you entered is palindrome"
else:
 print "number you entered is not a palindrome"


