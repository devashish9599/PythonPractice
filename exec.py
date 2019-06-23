class dev(Exception):
    pass 
    def fun(self):
        try:
            a=10
            b=0
            c=b/a
    
            raise dev
        except dev:
            print("ZeroDivisonError")
class er(dev):
    def fu(self):
        a=20
        b=10
        c=a+b
        print(c)
x=er()
x.fu()
x.fun()
