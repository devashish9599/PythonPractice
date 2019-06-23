a=input("enter the initial value of the interval: ")
b=input("enter the final value of the interval: ")
f=0
while a<b:
    f=0
    for i in range(2,a):
        if a%i==0:
            f=1
            break

    if f==0:
        print a
    a=a+1
