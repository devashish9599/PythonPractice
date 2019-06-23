a=[[12,45,5],
     [12,45,5],
     [12,6,68]]
c=0
f=0
g=0
for j in range(len(a)):
    f=f+1
    g=g+1
for i in range(len(a)):
    for j in range(len(a)):
        if(a[f][g]==a[i][j]):
           c=c+1
           print c
