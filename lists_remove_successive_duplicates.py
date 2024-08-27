def remove_successive_duplicate(int_list: list):
    i = 0
    
    while i < (len(int_list)-1):
        if int_list[i] == int_list[i+1]:
            int_list.pop(i+1)
        else: 
            i = i + 1    
    return int_list


def main():
    number_of_input = int(input("Enter the number of input: "))
    new_list = []
    for i in range(number_of_input):
        new_value = int(input("Enter a value: ")) 
        new_list.append(new_value)
    print((remove_successive_duplicate(new_list)))

if __name__ == "__main__":
    main()    