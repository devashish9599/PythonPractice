a=input("enter the string")
l=input("enter the second string")
z=len(l)
b=input("enter the character to be searched in first string")
count2=0
c=input("enter the character to be searched in second string")
x=len(a)
count=0

for i in range(0,x):
 if(a[i]==b):
  count=count+1
print count,"times is",b

for j in range(0,z):
 if(l[j]==c):
  count2=count2+1
print count2,"times is",c 