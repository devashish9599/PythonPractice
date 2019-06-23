class date:
    def day(self):
        a=int(input("enter the day"))
        print(a)
    def month(self):
        b=int(input("enter the month"))
        print(b)
    def year(self):
        c=int(input("enter the year"))
        print(c)
class advance(date):
    def day(self):
        a=a+1
        print(a)
    def month(self):
        b=b+1
        print(b)
    def year(self):
        c=c+1
        print(c)
x=advance()
x.day()
x.month()
x.year()