a=[0,0,0,0,0,0,0]
d=[0,0,0,0,0]
x=input("enter the lenght")
print "enter the brand names"
for i in range(0,x):
    a[i]=input("")
for k in range(0,x):
    b=len(a[k])
    print b
    d[k]=b
for j in range(0,x-1):
    for k in range(0,x-1):
        if(d[k]>d[k+1]):
            temp=d[k+1]
            d[k]=d[k+1]
            d[k+1]=temp
for l in range(0,x):
    print d[l]


    
