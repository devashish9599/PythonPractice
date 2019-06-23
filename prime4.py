a=input("enter the initial value")
b=input("enter the final value")
print "numbers are"
for i in range(a,b):
    f=0
    for j in range(2,i):
        if(i%j==0):
            f=1
    if(f==0):
        
        print i
    a=a+1
        
           
