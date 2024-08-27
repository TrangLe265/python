number_of_int = int(input("How many integers: "))
list_of_int = []

for i in range(number_of_int):
    new_int = int(input("Enter an integer: "))
    list_of_int.append(new_int)

list_of_int.reverse()
print()
print(*list_of_int, sep = " ")