# Extracting the words
with open("5_letter_words.txt") as f:
    words = [word.replace('\n', '') for word in f.readlines()]

# Getting probability of a letters in a position of the words
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
prob = dict()

for i in alphabet:
    prob[i] = [0, 0, 0, 0, 0]

for i in words:
    ind = 0
    for l in [*i]:
        prob[l][ind] += 1
        ind += 1

for i in alphabet:
    for k in range(5):
        prob[i][k] = prob[i][k]/len(words)

