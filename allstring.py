a=input("enter the string to be checked")
z=len(a)
b=['a','s','d','r','e','d','j']
count=[0,0,0,0,0,0]
x=int(input("enter the number of words to be checked"))

for i in range(0,x):
 b[i]=input("enter the words you need to find")

for i in range (0,x):
 count=0 
for j in range(0,z):
  if(a[i]==b[i]):
    print "for this varibale",b[i],"value become ,",count 
    count=count+1


