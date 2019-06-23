a=input("enter the initial value: ")
b=input("enter the final vlalue: ")
print "prime numbers between",a,"to",b,"are"
for i in range(2,b):
 for j in range(2,i):
  if i%j==0:
   break
  else:
   if i==j+1:
    if i>=a:
     print i,
  