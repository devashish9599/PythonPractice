amount=input("enter the amount to be withdrawn")
balance=50000
if(amount<=balance):
 if(amount>=2000)or(amount<=2000):
  print "machine doesnt have 2000rs note,press 1 to continue and 2 to end"
  choice=input("enter your choice")
  if(choice==1):
   a=amount/500
   b=amount%500
   c=b/100
   d=b%100
   print "you get /t",a,"five hundred note/s",c,"hundred note/s",d,"cant withdraw this amount"
else:
 print "you dont have sufficient balance"