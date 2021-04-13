#check whether the given year is leap yearo r not.if year is leap year print"LEAP YEAR"else print "COMMON YEAR'.
#hint:a year is a leap year if its number is excatly divisible by 4 and is not exactly divisible by 100.
given_year=int(input("enter the year:"))
if given_year % 4 == 0 and given_year % 100 !=0 or given_year % 400 == 0:
    print("LEAP YEAR")
else:
    print("COMMON YEAR")
