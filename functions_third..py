from decimal import Decimal

def compute_discount(price: float, discount: float):
    return Decimal(price*discount/100)

def main():
    price = float(input("Enter price: "))
    discount = float(input("Enter discount percentage: "))
    print(f"The discount is {(compute_discount(price,discount)):.2f} euros")

main()
