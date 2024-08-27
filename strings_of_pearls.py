string_1 = (input("Enter first string: ")).lower()
count = 0

if string_1 == "quit":
    print("\nBye!")
else: 
    while string_1 != "quit":
        if string_1 == "pearl": 
            count += 1
        string_1 = input("Enter next string: ").lower()
    print(count, "pearls\nBye!")


