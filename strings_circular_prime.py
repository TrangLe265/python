import math

def is_prime(number : int):
    if number < 2:
        return False
    else:
        for i in range(2,int(math.sqrt(number))+1,1):
            if (number % i == 0):
                return False  
        return True
    
def is_circular_prime(number: int):
    number_string = str(number)
    count = 0
    for i in range(len(number_string)):
        if not is_prime(int(number_string)) :
            return False
        number_string = number_string[1:] + number_string[0]
    return True
   
    
def main():
    number = int(input("Enter a positive integer: "))
    if is_circular_prime(number) == True:
        print(number,"is a circular prime")
    else:
        print(number,"is not a circular prime")

main()