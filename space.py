a=input("enter the string ")
class func:
    def __init__(self,name):
        self.name=name
    def show(self):
        space=" "
        d=[]
        print a[0],
        for i in range(0,len(a)):
         if space in a[i]:
            d=a[i+1]
            print d,
            
x=func(a)
x.show()
