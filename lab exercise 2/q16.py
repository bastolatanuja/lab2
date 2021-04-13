#write a python program to sum of three given integer.however,if two values are equal sum will be zero.
a=int(input("enter othe number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number: "))
sum=a+b+c
if a==b or b==c or a==c:
    print("the sum is zero")
else:
    print ("the sum is",sum)


def sum(a,b,c)  :
    if a==b or b==c or c==a:
        sum=0;
    else:
        sum=(a+b+c)
        return sum

x,y,z=[int(a) for a in input("enter three number: ").split(",")]
print(sum(x,y,z))