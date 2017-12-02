import os
import sys

challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

challenge_rows = challenge_data.split('\n')
total = 0
for row in challenge_rows:
    if (len(row) > 0):
        challenge_row = row.split(' ')
        challenge_row_numbers = list(
            int(s) for s in list(map(int, challenge_row))
        )
        minimum_value = min(challenge_row_numbers)
        maximum_value = max(challenge_row_numbers)
        total += maximum_value - minimum_value

print(total)
