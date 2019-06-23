a=[[12,34,56],
     [12,45,3]]
count=0
for j in range(len(a)):
    for i in range(len(a)):
        for k in range(len(a)):
            if(a[i][j]==a[k][j]):
                count=count+1
print count
