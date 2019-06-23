a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x=int(input("enter the range of the desired data : "))
print "enter the data :-"
for i in range(x):
    a[i]=int(input(" "))
for j in range(0,x):
    for j in range(0,x-1):
        if(a[j]<a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print "data in descending order is :- "
for k in range(0,x):
    print "(",
    print a[k],
    print ")",
for l in range(0,x):
    for n in range(0,x-1):
        if(a[n]>a[n+1]):
            temp1=a[n]
            a[n]=a[n+1]
            a[n+1]=temp1
print ""
print "data in ascending order is :- "
for s in range(0,x):
    print "(",
    print a[s],
    print ")",
            
