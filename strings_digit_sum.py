string = input("Enter a string: ")
sum = 0

for c in string: 
    if c.isdigit():
        sum += int(c)

print("\nThe sum of digits is",sum )