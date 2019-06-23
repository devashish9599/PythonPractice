c=input("enter any arithmetic operator (+,-,*,/)  ")
a=input("enter the first number: ")
b=input("enter the second number: ")
if c=="+":
    sum=(a+b)
    print sum
elif c=="-":
    diff=a-b
    print diff
elif c=="*":
    mul=a*b
    print mul
elif c=="/":
    div=a/b
    print div
else:
    print "check your choice"
    
