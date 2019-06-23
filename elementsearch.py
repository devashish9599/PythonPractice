a=[[0,0,0],
      [0,0,0],
      [0,0,0]]
   
b=[]
count=[0,0,0,0,0,0,0,0,0]
       
for i in range(len(a)):
       for j in range(len(a)):
         a[i][j]=input("elements: ")
       
for k in range(0,3):
      b=b+a[k]
print b
       
for i in range(0,9):
       for j in range(0,3):
           for k in range(0,3):
               if(b[i]==a[j][k]):
                   count[i]=count[i]+1

print "\n"                     
for k in range(0,9):
       print "element",b[k],"is",count[k],"times"
       
       
       
