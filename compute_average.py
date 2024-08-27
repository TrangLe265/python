from decimal import Decimal

sum = 0
x = Decimal(input("Enter first number: "))
if x == 0:
    print("Nothing to be calculated: ")
while x < 0 or x >0:
    sum = sum + x
    x = Decimal(input("Enter next number: "))

