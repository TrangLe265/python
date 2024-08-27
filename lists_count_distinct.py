def count_distinct(list_of_input: list):
    list_of_input = list(set(list_of_input))
    count_distinct = len(list_of_input)
    return count_distinct

def main(): 
    number_of_input = int(input("Enter the number of inputs: "))
    list = []
    for i in range(number_of_input):
        new_input=input("Insert input: ")
        list.append(new_input) 

    print(count_distinct(list))


if __name__ == "__main__":
    main()
