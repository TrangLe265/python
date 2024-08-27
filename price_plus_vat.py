try:
    price = float(input("Enter price: "))
    vat_price = float(price * 1.24)
    print(f"The price with VAT is {vat_price:.2f}")
except ValueError:
    print("Invalid price")