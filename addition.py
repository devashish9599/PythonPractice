sum=0
c1=0
c2=0
a=input("enter the first number")
b=input("enter the second number")
for i in range(2,a):
 for j in range(2,b):
     if (a%i==0)and(b%j==0):
        c1=1
        c2=1
        print "number entered is not prime"
     else:
        sum=a+b
print sum
