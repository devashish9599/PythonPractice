a=input("enter the string")
c=0
x=len(a)
print x
for i in (enumerate(a)):
    print i
for j in i:
    for k in range(0,9):
        if(a[j]==k):
            c=c+1
print c
