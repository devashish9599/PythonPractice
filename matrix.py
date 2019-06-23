x=[1,23,4,5,7,4,5,6]
y=[4,5,6,6,8,4,8,6]
result=[0,0,0,0,0,0,0,0]
z=input("enter the size of rows")
for i in range(0,z):
    x[i]=input("enter the elements of row")
k=input("enter the size of columns")
for j in range(0,k):
    y[i]=input("enter the elements of columns")
for i in range(0,z):
    for j in range(0,k):
        result=x[i][j]+y[i][j]
for r in result:
    print r
