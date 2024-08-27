def double_factorial(x: int):
    output = 1
    if x == 0: 
        output = 1
    elif x == 1: 
        output = 1
    else:
        if x%2 == 1:
            for i in range(1,x+1,2):
                output *= i
        else:
            for i in range(2,x+1,2):
                output *= i
    return output
def main():
    for x in range(0,10):
        print(f"{x}!! = {double_factorial(x)}")
main()
