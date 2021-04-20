#given a three digit number.find the sum of its digits.
num=int(input("enter the number:"))
first_digit=num%10
num=num//10
second_digit=num%10
num=num//10
third_digit=num%10
sum=first_digit+second_digit+third_digit
print(f"the sum of the digit is",sum)
