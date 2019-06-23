a=[1,3,4,34,5,6,56]
temp=0
x=input("enter the number of elements to be entered")
for i in range(0,x):
    a[i]=input("enter the numbers to be printed in ascending order")
for j in range(0,i+1):
 if a[j+1]<a[j]:
  a[j+1]=temp
  a[j+1]=a[j]
  a[j]=temp
  print j
        
        
