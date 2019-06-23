a=[0,0,0,0]
x=len(a)
temp=0
mi=a[0]
for k in range(0,x):
    a[k]=input("enter the elements")
for i in range(0,x):
    for j in range(0,x-1):
        if(mi>a[j+1]):
            mi=a[j+1]
            temp=mi
            print a[i]
