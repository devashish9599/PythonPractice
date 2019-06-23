def armstrong(n):
    temp=n
    s=0
    while(n!=0):
        c=n%10
        s=s+(c*c*c)
        n=n/10
    if(s==temp):
     print "number is armstrong"
    else:
     print "number is not armstrong"
n=input("enter the number")
armstrong(n)
