import os
import sys

challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

step_interval = int(challenge_data)
current_position = 0
steps = [0]
for i in range(1, 2018):
    for step in range(step_interval):
        current_position += 1
        current_position = current_position % len(steps)
    current_position += 1
    steps.insert(current_position, i)
print(steps[current_position + 1])
