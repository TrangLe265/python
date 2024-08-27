from urllib.request import urlopen 
url = "https://www.mit.edu/~ecprice/wordlist.10000" 
word_list = urlopen(url).read().splitlines() 
print(f"{len(word_list)} words")

sum = 0
word_count = 0

for i in range(len(word_list)):
    sum += len(word_list[i])
    word_count += 1

average_length = float(sum/word_count)

print(f"The average word length is {average_length}")

counters = [0] * 23

for x in range(len(word_list)):
    counters[len(word_list[x])] += 1

print("Length count")

for  y in range(1,len(counters)):
    print (f"{y:2d} {counters[y]:4d}")