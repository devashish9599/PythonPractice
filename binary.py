a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x=input("lst len")
temp=0
print "enter elements"
for i in range(0,x):
    a[i]=input("")
for i in range(0,x-1):
    for j in range(0,x-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print "\n"
print "data sort"
for k in range(0,x):
    print a[k]
item=input("item search")
s=0
l=x
mid=(s+l)/2
for i in range(0,x):
    if(item<a[mid]):
        s=0
        l=mid-1
        mid=(l+s)/2
        if(item==a[mid]):
          print "item get"
    elif(item>a[mid]):
        s=mid+1
        l=x
        mid=(l+s)/2
        if(item==a[mid]):
          print "item get"
    if(item==a[mid]):
        print "item get"
        
