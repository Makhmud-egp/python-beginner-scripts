
words = {} # to store word counts

# take user input, convert to lower(), and split into a list of words
sentence = input("Enter a sentece: ").lower().split()

# loop through each word in the sentence
for word in sentence:
    if word in words:
        # if the word is already in the dict, + 1 more count
        words[word] += 1
        
    else:
        # else start count with 1
        words[word] = 1

# loop through each key and value in the dict and print them out
for key, value in words.items():
    print(f"{key}: {value}")



