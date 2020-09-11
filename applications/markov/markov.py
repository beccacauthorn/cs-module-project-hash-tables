import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
word_dict = {}
list_of_words = words.split()
for i in range(len(list_of_words) - 1): 
    # add the next word to word_dict[word]
    curword = list_of_words[i]
    nextword = list_of_words[i + 1]

    if curword not in word_dict:
        word_dict[curword] = []

    word_dict[curword].append(nextword)


# TODO: construct 5 random sentences
# Your code here
for x in range(5): 
    current = random.choice([w for w in list_of_words if w[0].isupper()])
    punctuation = '`.?!"`'
    while True:
        print(current, end=' ')
        nextword = random.choice(word_dict[current])
        last_char = nextword[-1]
        if last_char in punctuation:
            break
        current = nextword
    print(nextword)
