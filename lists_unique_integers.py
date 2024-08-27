int_list = []
for i in range(5):
    new_int = int(input("Enter an integer: "))
    int_list.append(new_int)

distinct_list = sorted(set(int_list))
print(*distinct_list, sep = ", ")
int_list.sort()
print(*int_list, sep =", ")