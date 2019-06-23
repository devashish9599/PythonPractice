a=input("enter the string")
d=len(a)
c=[0,0,0,0,0]
b=['0','0','0','0','0','0','0','0','0','0']
x=input("enter the number of alphabets to be checked")
for i in range(0,x):
    b[i]=str(input("enter the alphabets"))
for j in range(0,d):
    if(b[i]==a[j]):
        c=c+1
        print c
