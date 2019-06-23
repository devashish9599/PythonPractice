def sort(a):
    for i in range(x):
        a[i]=input(" ")
    temp=0
    for i in range(0,x-1):
        for j in range(0,x-1):
            if(a[j]>a[j+1]):
                temp=a[j+1]
                a[j+1]=a[j]
                a[j]=temp
    print "ascending list"
    for k in range(0,x):
        print a[k]
a=[0,0,0,0,0,0,0]
x=input("enter the range")
sort(a)
