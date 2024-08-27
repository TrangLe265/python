def second_largest(list_name:list):
    list_name = list(set(list_name))
    if len(list_name) < 2:
        return None
    else: 
        max_value = max(list_name)
        list_name.remove(max_value)
        second_largest = max(list_name)
        return second_largest

def main():
    number_of_input = int(input("Enter the number of input: "))
    new_list = []
    for i in range(number_of_input):
        new_value = int(input("Enter a value: ")) 
        new_list.append(new_value)
    print(second_largest(new_list))

if __name__ == "__main__":
    main()
