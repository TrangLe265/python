def common_members(list_1:list, list_2: list):
    common_members = 0
    for i in range(len(list_1)): 
        for x in range(len(list_2)):
            if list_1[i] == list_2[x]:
                common_members += 1
    
    if common_members == 0:
        return False
    else:
        return True

def main():
    number_of_input_list_1 = int(input("Enter number of inputs for list 1: "))
    list_1 = []
    for i in range(number_of_input_list_1):
        new_int = int(input("Enter an integer: "))
        list_1.append(new_int)
    
    number_of_input_list_2 = int(input("Enter number of inputs for list 2: "))
    list_2 = []
    for x in range(number_of_input_list_2):
        new_int = int(input("Enter an integer: "))
        list_2.append(new_int)
    
    print(common_members(list_1,list_2))

if __name__ == "__main__": 
    main()
    