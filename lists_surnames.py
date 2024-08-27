surnames_list = []

surname = input("Enter a surname (ok ends): ")

while surname != "ok":
    surnames_list.append(surname)
    surname = input("Enter a surname (ok ends): ")

surnames_list = list(set(surnames_list))
surnames_list.sort()
print()
print(*surnames_list, sep =", ")
