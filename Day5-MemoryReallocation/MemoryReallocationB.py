import os
import sys

challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

memory_banks = [
    int(bank_value) for bank_value in challenge_data.split('\n')[0].split(' ')
]

stored_configurations = []
stored_configurations.append(memory_banks)
found_duplicate_configuration = False

steps = 0
cycle = None
while not found_duplicate_configuration:
    new_memory_banks_configuration = list(stored_configurations[-1])
    steps += 1
    highest_bank_index, \
        highest_bank_value = max(
            enumerate(new_memory_banks_configuration), key=lambda v: v[1]
        )
    current_bank_index = highest_bank_index
    new_memory_banks_configuration[highest_bank_index] = 0

    for i in range(highest_bank_value, 0, -1):
        current_bank_index = (current_bank_index + 1) \
            % len(new_memory_banks_configuration)
        new_memory_banks_configuration[current_bank_index] += 1

    if new_memory_banks_configuration in stored_configurations:
        cycle = steps \
            - stored_configurations.index(new_memory_banks_configuration)
        found_duplicate_configuration = True
    stored_configurations.append(new_memory_banks_configuration)

print(steps, cycle)
