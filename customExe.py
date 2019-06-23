class first(Exception):
    def add(self):
        a=10
        b=0
        c=a/b
        print c
x=first()
class second(first):
    pass
try:
    if ZeroDivisionError in first:
        raise two
except second:
    print "error"
    
