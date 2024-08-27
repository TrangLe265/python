string = input("Enter a string: ").strip()
char = input("Enter a character: ")
start_point = 0
for i in range(len(string)): 
    if string[i] == char:
        output = string[i:i+4]
        if len(output) == 4:
            print(output)


