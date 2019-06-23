a=input("enter the year to be checked: ")
if(a>2018):
 if(a%4==0):
    print a,"year entered WILl be leap year"
 else:
    print a,"year entered WILL be not a leap year"
elif(a<2018):
    if(a%4==0):
        print a,"year WAS a leap year"
    else:
        print a,"WAS not a leap year"
