a=[[12,56,100],[30,49,60]]
temp=0
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if(a[j]<a[j+1]):
            temp=a[j+1]
            a[j]=[j+1]
            a[j+1]=temp
for k in range(len(a)):
    print a[k]
