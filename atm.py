amount=int(input("enter the amount"))
balance=3000
if(amount>balance):
 print "press one to continue,press two to end"
 choice=int(input("enter your choice"))
 if(choice==1):
  a=amount%500
  b=amount/500
  c=b%100
  d=c/100
  print "you have\t",a,"500 note/s",c,"hundred note/s",d,"this amount can not be withdraw"
 else:
  print "thank you for comming"

 