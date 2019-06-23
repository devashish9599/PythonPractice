amount=int(input("enter the amount"))
balance=5000000
if(amount<=balance):
 if(amount<=2000)or(amount>=2000):
  print "machine do not have 2000 note,press 1 to proceed and 2 to end"
  choice=int(input("enter your choice"))
 if(choice==1):
  a=amount/500
  b=amount%500
  c=b/100
  d=b%100
  print "you get\t",a,"five hundred notes\t",c,"hundred notes",d,"in tens"
else:
 print "sorry you have insufficient balance"