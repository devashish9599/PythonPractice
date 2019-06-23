a=[0,0,0,0,00,0,0,0,0]
x=input("enter how many you want to ceck")
temp=0
for i in range(0,x):
 for j in range(i,x):
  if a[i]>a[j+1]:
   a[i]=temp
   a[i]=a[j+1]
   a[j+1]=temp
   print i