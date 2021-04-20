#given three integers ,print the smallest one.(three integers should be user input)
num1=int(input("enter the number: "))
num2=int(input("enter the second number: "))
num3=int(input("enter the third number: "))
if num1<num2 and num1<num3:
    print(f"the {num1} is the smallest")
elif num2<num3  and num2<num1:
    print(f"the {num2}is the smallest")
else:
    print(f"the {num3} is the smallest")