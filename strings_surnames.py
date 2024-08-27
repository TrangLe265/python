number_of_names  = int(input("How many surnames? "))
name_list = []

for i in range(number_of_names):
    name = input("Enter a surname: ").capitalize() 
    name_list.append(name)

name_list = list(set(name_list))
print()
print(*sorted(name_list), sep =" ")