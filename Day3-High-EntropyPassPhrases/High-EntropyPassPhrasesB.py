import os
import sys
from itertools import permutations


def anagrams_present(words):
    for word in words:
        word_permutations = [''.join(p) for p in permutations(word)]
        for permutation in word_permutations:
            if permutation == word and words.count(permutation) == 1:
                continue
            if words.count(permutation) > 0:
                return True
    return False


challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

challenge_rows = challenge_data.split('\n')
del challenge_rows[-1]

rows_with_anagrams = 0
for row in challenge_rows:
    words = row.split(' ')
    word_anagrams = anagrams_present(words)
    if word_anagrams > 0:
        rows_with_anagrams += 1

print(len(challenge_rows) - rows_with_anagrams)
