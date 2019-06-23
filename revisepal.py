num=input("enter the number to be reversed")
b=0
temp=num
while(num!=0):
 a=num%10
 b=b*10+a
 num=num/10
print b
if(temp==num):
 print "the number entered is palindrome"
else:
 print "the number you entered is not palindrome"