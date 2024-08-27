try:
    x = (input("Enter an integer: "))
    x = int(x)
    print("OK")
except ValueError:
    print(f"'{x}' is not an integer")
