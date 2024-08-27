is_valid = False

x = input("Enter a month number: ")

while not is_valid:
    try:
       x = int(x)    
    except ValueError:
        print(f"'{x}' is not a valid month number")
        x = input("\nEnter a month number: ")
    else:
        if 1 <= x <= 12:
            print("OK")
            is_valid = True
        else:
            print(f"{x} is not a valid month number")
            x = input("\nEnter a month number: ")
        
        
