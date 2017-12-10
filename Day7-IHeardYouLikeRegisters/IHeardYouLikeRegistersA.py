import os
import sys
import operator

challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

instructions = challenge_data.split('\n')

comparisons = {
    ">": operator.gt,
    ">=": operator.ge,
    "<": operator.lt,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne
}

registers = {}

for instruction in instructions:
    instruction = instruction.split(' ')
    operated_register = instruction[0]
    command = instruction[1]
    command_value = int(instruction[2])
    conditional_register = instruction[4]
    conditional = comparisons[instruction[5]]
    conditional_value = int(instruction[6])
    operated_register_value = registers.get(operated_register, 0)
    conditional_register_value = registers.get(conditional_register, 0)

    if command == 'dec':
        command_value = -command_value

    if conditional(conditional_register_value, conditional_value):
        registers[operated_register] = registers.get(operated_register, 0) \
            + command_value

highest_register_index = max(registers.items(), key=operator.itemgetter(1))[0]

print(registers[highest_register_index])
