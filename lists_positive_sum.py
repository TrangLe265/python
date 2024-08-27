list_of_int = []

for i in range(5):
    new_int = int(input("Enter an integer: "))
    list_of_int.append(new_int)

sum = 0
count = 0

for i in range(5):
    if list_of_int[i] > 0:
        sum += list_of_int[i]
        count +=1

if count == 0:
    print("\n0")
elif count > 0:
    print(f"\n{sum}")
