import os
os.mkdir("lol")
os.chdir("lol")
f=open("eve.txt","w")
for i in range(5):
    n=int(input("enter the number"))
    f.write(str(n))
f.readline()
f.close()