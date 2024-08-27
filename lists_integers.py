list_of_int = []

for i in range(5):
    new_int = int(input("Enter an integer: "))
    list_of_int.append(new_int)

list_of_int.sort(reverse=True)
print()
print(*list_of_int, sep = " ")

print(f"count: {len(list_of_int)}")
print(f"min:{min(list_of_int):2d}")
print(f"max:{max(list_of_int):2d}")
print(f"sum:{sum(list_of_int):2d}")