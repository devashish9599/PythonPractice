a=[12,34,6,78,44,66,4]
x=len(a)
temp=0
for i in range(0,x):
    for j in range(0,x-1):
        min=a[i+1]
        if(min<a[i]):
            temp=a[i+1]
            a[i+1]=min
            min=temp
    print a[i]
        
