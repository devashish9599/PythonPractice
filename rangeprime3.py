a=int(input("enter the initial value"))
b=int(input("enter the final value"))
while(a<b):
 f=0
 for i in range(2,a):
     if(a%i!=0):
         f=1
         break
     if(f==1):
      print a
     else:
      print "sd"
    
    
