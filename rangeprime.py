a=input("enter the initial stage")
f=0
b=input("enter the final stage")
while(a<b):
    for i in range(2,a):
        if a%i==0:
         f=1
    if f==1:
     print a
    else:
     f=0
