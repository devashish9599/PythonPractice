num=input("enter the number")
temp=num
b=0
while(num!=0):
 a=num%10
 b=b*10+a
 num=num/10
print b
if(b==temp):
 print "number is palindrome"
else:
 print "number is not palindrome"