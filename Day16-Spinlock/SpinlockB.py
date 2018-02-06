import os
import sys

challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

step_interval = int(challenge_data)
current_position = 0
current_1_value = None
for step in range(1, 50000001):
    current_position = (current_position + step_interval) % step + 1
    if current_position == 1:
        current_1_value = step

print(current_1_value)
