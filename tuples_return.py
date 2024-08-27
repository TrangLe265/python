def pow_2_3(number: int):
    tuple = (pow(number,2),pow(number,3))
    p2,p3 = tuple
    return tuple
    

def main(): 
    x = int(input("Enter an integer: ")) 
    p2, p3 = pow_2_3(x) 
    print(p2) 
    print(p3) 
    
if __name__ == "__main__":
    main() 