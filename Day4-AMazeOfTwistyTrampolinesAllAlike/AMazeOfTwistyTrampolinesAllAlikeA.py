import os
import sys

challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

instructions = challenge_data.split('\n')

i = 0
steps = 0
while i < len(instructions):
    steps += 1
    jump_value = int(instructions[i])
    incremented_instruction = jump_value + 1
    instructions[i] = str(incremented_instruction)
    i = i + jump_value

print(steps)
