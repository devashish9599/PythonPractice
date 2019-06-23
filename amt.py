amount=int(input("enter the amount\t"))
balance=90000
if(amount<=balance):
 if(amount<=2000)or(amount>=200):
  print "machine do not have 2000 note,press one to proceed and 2 to end"
  choice=int(input("enter your choice"))
 if(choice==1):
  a=amount/500
  b=amount%500
  c=b/100
  d=b%100
  print "money design is=\t",a,"five hundred note",c,"hundred note",d,"cant withdraw this amount"
else:
 print "sorry you have insufficient balance"  
  
 
