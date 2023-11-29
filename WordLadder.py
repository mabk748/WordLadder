# Extracting the words
with open("5_letter_words.txt") as f:
    words = [word.replace('\n', '') for word in f.readlines()]

# is_thesame = []
# for i in words:
#     count = 0
#     for j in words:
#         if i == j:
#             count += 1
#     is_thesame.append(count)
# print(is_thesame)


# words = ["hot", "bit", "xyz", "dot", "lot", "log", "dog", "cog", "hox"]

# Getting probability of a letters in a position of the words
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
prob = dict()

for i in alphabet:
    prob[i] = [0 for _ in range(len([*words[0]]))]

for i in words:
    ind = 0
    for l in [*i]:
        prob[l][ind] += 1
        ind += 1

words_count = len(words)
for i in alphabet:
    for k in range(len(prob[i])):
        prob[i][k] = prob[i][k]/words_count

# print(prob)

# Finding neighbors

def are_adjacents(a: str, b: str):
    differences = 0
    for (la, lb) in zip(a, b):
        if la != lb:
            differences += 1
    return differences == 1

def neibors(word: str, list_of_words: list):
    return [other_word for other_word in list_of_words if are_adjacents(word, other_word)]

def finding_path(start: str, target: str, words: list):
    tar_prob = [(prob[i][ind], i, ind) for ind, i in enumerate([*target])]
    tar_prob.sort(key=lambda a: a[0], reverse=True)
    word_path = [start]
    found = [False for _ in range(len([*start]))]
    while target not in word_path:
        print(word_path)
        neibs = neibors(word_path[-1], words)
        for i, (a, b) in enumerate(zip([*target], [*word_path[-1]])):
            if a == b:
                found[i] = True
        print(found)
        print(neibs)
        if neibs == []:
            break
        for i in neibs:#F1
            # If 
            for j in tar_prob:#F2
                if j[1] == [*i][j[2]] and not found[j[2]]:
                    word_path.append(i)
                    print(i)
                    words.remove(i)
                    break#F2
            else:
                #If F2 terminate without breaking
                continue#F1
            #If F2 terminate with breaking 
            break#F1
        else:
            choices = []
            for i in neibs:
                for ind, j in enumerate([*i]):
                    if not found[ind]:
                        choices.append((prob[j][ind], j, ind))
                        choices.sort(key=lambda a: a[0], reverse=True)
            for i in neibs:
                if [*i][choices[0][2]] == choices[0][1]:
                    word_path.append(i)
                    print(i)
                    words.remove(i)
    return word_path

print(finding_path("abend", "gooks", words))
    