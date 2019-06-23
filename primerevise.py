a=int(input("enter the number to be checked"))
f=0
for i in range(2,a):
 if(a%i==0):
  f=1
  break
if(f==1):
 print "number is not prime"
else:
 print "number entered is prime"

