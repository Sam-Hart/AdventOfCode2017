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
    challenge_row = row.split(' ')
    challenge_row_numbers = list(
        int(s) for s in list(map(int, challenge_row))
    )
    for index, number in enumerate(challenge_row_numbers):
        next_index = index + 1
        if len(challenge_row_numbers) >= next_index:
            for reduced_number in challenge_row_numbers[next_index:]:
                if (number % reduced_number == 0):
                    total += number // reduced_number
                    break
                elif (reduced_number % number == 0):
                    total += reduced_number // number
                    break

print(total)
