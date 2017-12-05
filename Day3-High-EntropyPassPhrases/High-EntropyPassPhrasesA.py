import os
import sys

challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

challenge_rows = challenge_data.split('\n')

rows_with_duplicates = 0
for row in challenge_rows:
    words = row.split(' ')
    row_duplicates = [x for x in words if words.count(x) > 1]
    if len(row_duplicates) > 1:
        rows_with_duplicates += 1

print(len(challenge_rows) - rows_with_duplicates)
