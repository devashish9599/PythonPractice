a=[[0,0],
      [0,0]]

b=[[2,3],
      [5,6]]


c=[[0,0],
      [0,0]]
print "enter the nested list elements"
for i in range(0,2):
    for j in range(0,2):
        a[i][j]=input(" ")
for j in a:
    print j
    print "\n"
for j in b:
    print j

print "addition"
for i in range(len(a)):
    for j in range(len(a)):
        c[i][j]=a[i][j]+b[i][j]
for k in c:
    print k

print "subtraction"
for i in range(len(a)):
    for j in range(len(a)):
        c[i][j]=a[i][j]-b[i][j]
for k in c:
    print k

print "multiplication"
for i in range(len(a)):
    for j in range(len(a)):
        for k in range(0,2):
            c[i][j]=c[i][j]+a[i][k]*b[k][j]
for v in c:
    print v
