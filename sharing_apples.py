apples = int(input("How many apples? "))
children = int(input("How many children? "))

apple_per_child = apples//children
leftover = apples%children

print(f"Each child will get {apple_per_child} apples.")
print(f"There will be {leftover} leftover apples.")