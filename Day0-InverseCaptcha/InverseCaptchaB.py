import os
import sys

challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

challenge_number = challenge_data.split("\n")[0]

value = 0
for index, char_digit in enumerate(challenge_number):
    next_index = (index + (len(challenge_number) // 2)) % len(challenge_number)
    if char_digit == challenge_number[next_index]:
        value += int(challenge_number[next_index])

print(value)

# This was a pretty cool one liner I found
print(sum(int(x[0]) for x in zip(challenge_number, challenge_number[len(challenge_number)//2:] + challenge_number[:len(challenge_number)//2 - 1]) if x[0] == x[1]))
