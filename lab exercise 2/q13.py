#given a positive real number,print its fractional part.
import math
number=float(input("enter the positive real number:"))
print(math.modf(number))

number2 = float(input("Enter the number: "))
number3 = int(number2)
division_part = number2 - number3
print(f"The division part of {number2} is {division_part}")