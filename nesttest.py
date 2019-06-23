a=[[1,2,3],
      [4,4,4],
      [6,7,8]]
x=len(a)
print x
f=0
d=0
c=int(input("search element"))
for i in range(0,x):
        if c in a[i]:
            f=1
            d=d+1
            print d
            continue

if f==1:
    print "found"
    print "it is present",d,"times"
else:
    print "not found"
    
