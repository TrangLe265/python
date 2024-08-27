list = []
for i in range(7):
    integer = input("Enter an integer: ")
    list.append(integer)

i = 0

while i < len(list):
   list[i], list[i+1] = list[i+1],list[i]
   i = i+2
   
print(list)


