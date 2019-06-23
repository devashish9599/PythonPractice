a=int(input("enter the number to be checked"))
x=len(str(a))
if(x==1):
 print "single digit number,can not compare with itself"
elif(x==2):
 z=a/10
 y=a%10
 if(z>y):
  print "greatest in the digit is",z
 else:
  print "greatest in the digit is",y
elif(x==3):
 r=a/100
 s=a%10
 h=(a/10)%10
 if(r>s)and(r>h):
  print "greatest is",r
 elif(s>r)and(s>h):
  print "greatest is",s
 elif(h>r)and(h>s):
  print "greatest is",h
else:
 print "working till 3 digits, SORRY"