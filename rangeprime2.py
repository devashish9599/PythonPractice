a=input("enter the initial number")
b=input("enter the final number")
f=0
while(a<b):
    for i in range(2,b):
        if  b%i==0:
            f=1
             break
    for j in range(a,b):
        if f==1:
            print "number is not prime",i
        else:
            print j
