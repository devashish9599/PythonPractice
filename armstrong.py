a=int(input("enter the number you want to check as an armstrong number"))
c=a
r=0
while(a!=0):
    z=a%10
    r=r+z*z*z
    a=a/10
print r
if(r==c):
    print "number you entered,according to me is armstrong"
else:
    print "number you entered,according to me is not armstrong number"
    
    
