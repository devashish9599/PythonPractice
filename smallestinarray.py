a=[5,4,3,2,1]
x=input("enter the range")
mi=a[0]
for i in range(0,x):
    a[i]=input("enter the elements") 
    a.sort()
    for i in range(0,x):
        if(mi<a[i]):
         mi=a[i]
print "smallest  number is",mi
