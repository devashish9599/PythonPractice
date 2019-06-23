a=[[2,43,5],
      [2,5,8]]
count=0

for i in range(len(a)):
    for j in range(len(a)):
        if(a[i][j]==a[i]):
            count=count+1
print count
            
            
