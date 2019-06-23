a=input("enter the initial of the range")
b=input("enter the final value of the range")
count=0
count1=0
for i in range(0,a):
    for j in range(i,b):
        if(j%2==0):
            count=count+1
            print "number of even numbers are",count
        else:
            count1=count1+1
            print "number of odd numbers are",count1