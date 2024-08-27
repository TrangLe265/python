string = input("Enter a string: ")
shorten_string = list(set(string))
if len(shorten_string) == len(string):
    print("No duplicates")
else:
    print("Contains duplicate(s)")