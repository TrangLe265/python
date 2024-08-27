try: 
    x = int(input("Enter a non-negative integer: "))
    double_factorial = 1
    if x < 0: 
        print("Please enter a non-negative integer")
    elif x == 0:
        print("0!! = 1")
    else:
        if x%2 == 1:
            for i in range(1,x+1,2):
                double_factorial *= i 
            print(f"{x}!! = {double_factorial}")
        else:
            for i in range(2,x+1,2):
                double_factorial *= i 
            print(f"{x}!! = {double_factorial}") 
except ValueError:  
    print("Not an integer!")