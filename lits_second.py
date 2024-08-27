word = input("Enter a word (quit ends): ")
word_list = []

while word != "quit": 
    word_list.append(word)
    word = input("Enter a word (quit ends): ")

word_list.sort()
print(*word_list, sep = "\n")