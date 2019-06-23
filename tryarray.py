print "enter 1 for odd even"
print "enter 2 for table"
print "enter 3 for palindrome"
print "enter 4 for reverse of a number"
print "enter 5 for sum"
print "enter 6 for divison"
choice=int(input("enter the repsective choice"))
if(choice==1):
 a=int(input("enter the digit"))
 if(a%2==0):
  print "number is even"
 else:
  print "number is odd"
elif(choice==2):
 b=int(input("enter the number for its multiples"))
 for i in range(1,11):
  print "multiples are",b*i
elif(choice==3):
 c=int(input("enter the number to  be checked"))
 d=0
 temp=c
 while(c!=0):
  e=c%10
  d=d*10+e
  c=c/10
 print d
 if(temp==d):
  print "number is palindrome"
 else:
  print "number is not palindrome"
elif(choice==4):
 z=int(input("enter the number to be reversed"))
 f=0
 temp1=z
 while(z!=0):
  e1=z%10
  d1=f*10+e1
  z=z/10
 print d
elif(choice==5):
 y=input("enter the first number")
 m=input("enter the second number")
 sum=y+m
 print sum
else:
 print "out of box"

 
