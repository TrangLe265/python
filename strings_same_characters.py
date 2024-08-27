string_1 = (input("Enter first string: ")).replace(" ", "").lower()
string_2 = (input("Enter second string: ")).replace(" ", "").lower()
if sorted(string_1) == sorted(string_2):
    print("Same characters")
else:
    print("Different characters")
