a=0
b=1
c=0
z=input("press the number till where you want to continue the fibonacci series")
print a,b
for i in range(1,z):
    c=a+b
    a=b
    b=a
    print c
    
