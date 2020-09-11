
def word_count(x):
    wordFreq = {}
    lower = x.lower()
    bad_chars = ['"',  ":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", ']', '{', '}', '(', ')', '*', '^', '&']
    for i in bad_chars:
        lower = lower.replace(i, '') 
    list_words = lower.split()
    for word in list_words:
        if word not in wordFreq:
            wordFreq[word] = 1
        else:
            wordFreq[word] += 1

    return wordFreq
    

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))