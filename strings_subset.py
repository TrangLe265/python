string_1 = input("Enter first string: ")
string_2 = input("Enter second string: ")

if len(string_2) == 0: 
    print("Nothing to be checked")
else:
    subset_count = 0
    string_2 = list(set(string_2))
    for c in string_2:
        if c in string_1:
            subset_count += 1
    if subset_count == len(string_2):
        print("Subset")
    else:
        print("Not subset")