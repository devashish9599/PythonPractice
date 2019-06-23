a=input("enter the string you want to check")
x=len(a)
flag=0
b=['s','a','s','f','t']
c=input("enter the number of words you want to test for")
for i in range(0,c):
 b[i]=input("enter the words you want to check in the entered string")
for q in range(0,c):
 count=0
 for j in range(0,x):
  if(a[j]==b[q]):
   count=count+1
 flag=0
 if(flag==0):
  print b[q],"is",count,"times"
 else:
  print b[q],"is",count
