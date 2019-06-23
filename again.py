a=input("enter the string")
z=len(a)
flag=0
b=['a','s','e','r','t','v']
x=input("enter the number of words you want to enter")
for j in range(0,x):
    b[j]=input("which word you want to find")
for q in range(0,x):
    count=0
    for i in range(0,z):
        if(a[i]==b[q]):
            count=count+1
            flag=0
        if(flag==0):
            print b[q],"is",count,"times"
        else:
            print b[q],"is",count
