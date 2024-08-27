print("=== Creating a dictionary ===")
dictionary = {}

engWord = input("Enter english word (quit ends): ").lower()
keepEntering = True

while keepEntering == True: 
    if engWord != "quit": 
        finWord = input("Enter finnish word: ").lower()
        dictionary[engWord] = finWord
        engWord = input("Enter english word (quit ends): ").lower()
    else: 
        keepEntering = False

print("\n=== Using a dictionary ===")

searchWord = input("Enter english word (quit ends): ").lower()
condition = True

while condition == True: 
    if (searchWord != "quit"):
        if  searchWord in dictionary: 
            print(dictionary[searchWord])
        else:
            print("Unknown word")
        searchWord = input("\nEnter english word (quit ends): ").lower()
    else: 
        condition = False