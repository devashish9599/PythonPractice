print "press 1 one for atm"
print "press 2 for reverse"
print "press 3 for string number"
choice=input("enter the choice as repected above")
if(choice==1):
    a=input("enter the amount to be withdrawn")
    balance=4000
    if(a<=4000):
     if(a<2000)or(a>2000):
      b=a/500
      c=a%500
      d=c/100
      e=d%100
      print b,"500",d,"100",e,"no change"
     else:
      print "you dont have sufficient balance"
elif(choice==2):
 print "you wish to reverse the number acc. to your choice"
 s=int(input("enter the number to be reversed"))
 q=0
 v=s%10
 q=q*10+v
 s=s/10
 print "the reversed number is",q
elif(choice==3):
       n=input("enter the string to be checked")
       t=len(n)
       b=['a','s','f','g','h','v']
       m=input("how many words you wish to check")
       for k in range(0,m):
        b[k]=input("enter those words")
        for j in range(0,m):
         count=0
         for i in range(0,t):
          if(n[i]==b[j]):
           count=count+1
           flag=1
         if(flag==0):
          print b[j],"is",count,"times"
         else:
          print b[j],"is",count
else:
 print "out of box choice"
       
            
            
