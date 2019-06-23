a=input("enter the string")
count=0
x=len(a)
for i in range(0,x):
 if(a[i]=="a"):
  count=count+1
  print "it is repeated",count,"times"
 else:
  print " "
 