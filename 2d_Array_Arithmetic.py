a=[[12,2],
     [5,3]]
b=[[1,2],
     [4,5]]
c=[[0,0],
     [0,0]]
print "addition"
for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]=a[i][j]+b[i][j]
for v in(c):
    print v   
print "subtraction"
for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]=a[i][j]-b[i][j]
for v in(c):
    print v    
print "multiplication"
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(0,2):
            c[i][j]=c[i][j]+a[i][k]*b[k][j]
for v in(c):
    print v
    

