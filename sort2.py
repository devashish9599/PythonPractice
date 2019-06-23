sort=[1,3,5,5,2,6,7,4,3,6]
x=int(input("enter the lenght"))
print "1) descending order"
temp=0
for k in range(0,x):
    sort[k]=float(input("enter the elements"))
    
for i in range(0,x-1):
    for j in range(0,x-1):
        if sort[j]<sort[j+1]:
            temp=sort[j]
            sort[j]=sort[j+1]
            sort[j+1]=temp
for c  in range(0,x):
    print sort[c]
print "2) ascending order"
for i in range(0,x-1):
    for j in range(0,x-1):    
         if sort[j]>sort[j+1]:
            temp=sort[j]
            sort[j]=sort[j+1]
            sort[j+1]=temp
for c  in range(0,x):
 print sort[c]


        
