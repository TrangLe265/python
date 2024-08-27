from decimal import Decimal 
interest_rate = Decimal(input("Enter interest rate: "))
tax = Decimal(input("Enter capital income tax rate: "))
deposit = Decimal(input("Enter initial deposit: "))
number_of_year = int(input("Enter number of years: "))

balance = deposit 
output = ""

for i in range(1,number_of_year+1):
    interest_amount = balance * interest_rate/100
    tax_amount = interest_amount * tax/100
    amount_added = interest_amount - tax_amount
    balance += amount_added
    output += (f"\nYear {i}: {balance:.2f}")

print(output)