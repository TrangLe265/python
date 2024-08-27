def sum_every_other(list_of_value: list):
    sum = 0; 
    length = len(list_of_value); 
    if length == 0: 
        return None
    else:
        for i in range(0,length,2):
            sum += list_of_value[i]; 
        return sum
        

def main(): 
    list_of_value = []

    number_of_int = int(input("Enter the number of values: "))
    for i in range(number_of_int):
        new_int = int(input("Enter an integer: "))
        list_of_value.append(new_int)
    
    print(sum_every_other(list_of_value))


if __name__ == "__main__": 
    main()