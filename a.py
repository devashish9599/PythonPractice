a=input("enter the string here: ")
c=0
x=len(a)
s=input("enter the alphabet to be checked in the string:")
for i in range(0,x):
    if(s==a[i]):
        c=c+1
print s,"is:",c," times"
