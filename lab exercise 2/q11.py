#for given integer x,print"true"if it is positive,print"false"if it is negative and print"zero".
#if it is 0.
num=int(input("enter the number:"))
if num<0:
    print(f"the {num} is negative")
elif num>0:
    print(f"the {num} is positive")
else:
    print(f"the {num} is 0")