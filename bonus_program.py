price = float(input("Enter the car's selling price: "))

if price < 50000:
    sales_bonus = price * (1/100)
    if sales_bonus < 200:
        sales_bonus = 200
if price >= 50000:
    sales_bonus = price * (1.5/100)

print(f"The bonus is {sales_bonus:.2f} euros.")