a=int(input("enter the first number\t"))
b=int(input("enter the seocnd number\t"))
c=int(input("enter the third number\t"))
if(a>b)and(a>c):
 print "largest is",a
elif(b>a)and(b>c):
 print "largest is",b
elif(c>b)and(c>a):
 print "largest is",c
else:
 print "all are equal"	