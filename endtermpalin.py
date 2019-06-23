a=input("enter the number")
temp=a
b=0
while(a!=0):
    c=a%10
    b=b*10+c
    a=a/10
print b
if(b==temp):
    print "number entered is a palindrome number"
else:
    print "number entere is not a palindroem number"
