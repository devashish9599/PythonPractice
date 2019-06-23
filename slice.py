a=[1,2,3,4,5,56,6,4,4,3]
b=[0,0,0,0,0,0,0,0,0,0]
c=[0,0,0,0,0,0,0,0,0,0]
c1=0
c2=0
x=input("enter the length")
print "now input one element and press enter"
for j in range(0,x):
    a[j]=input()
print "\n"
print "odd index list is:-"
for  i in range(0,x):
    if(i%2==0):
        c1=c1+1
        b[i]=a[i]
        print b[i]
print "number of odd elemnts:",c1
print "\n"
print "even index list is:-"
for k in range(0,x):
    if(k%2!=0):
        c2=c2+1
        c[k]=a[k]
        print c[k]
print "number of even elements:",c2
