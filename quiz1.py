a=[0,0,0,0]
x=input("enter the length")
for i in range(0,x):
    a[i]=input("enter the elements")
for k in a:
    print k,
for j in range(2,x+2):
    j=-j
    print a[j],
