class first:
    def add(self):
        a=10
        b=10
        c=a+b
        print(c)
class second(first):
    def sub(self,a,b):
        print(a-b)
x=second()
x.sub(12,5)

x.add(3,4)