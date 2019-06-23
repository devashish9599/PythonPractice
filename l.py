a=input("enter the string")
class first():
    def __init__(self, name):
        self.name=name
    def show(self):
        c=0
        d=0
        space=" "
        word=" "
        print self.name
        for i in range(len(a)):
            if space in a[i]:
                d=d+1
                if(a[i+1]=="l"):
                    for j in range(d,len(a)):
                        word=a[j]
                        if(word=="o"):
                            c=c+1
                            print c
x=first(a)
x.show
