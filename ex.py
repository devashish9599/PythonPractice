class first:
    def add(self):
        a=10
        b=9
        c=a-b
        return c
class second(first):
    def add(self):
        a=5
        b=3
        c=a+b
        return c
x=second()
print(x.add())
 
