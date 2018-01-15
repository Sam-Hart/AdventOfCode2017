import os
import sys

challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

noted_programs = challenge_data.split('\n')


def find_child_programs(program_id, exclude_ids=[]):
    child_programs = []
    child_programs += programs[program_id]
    for exclude_id in exclude_ids:
        if exclude_id in child_programs:
            child_programs.remove(exclude_id)
    exclude_ids += child_programs
    grouped_ids = child_programs
    for child_program in child_programs:
        grouped_ids += find_child_programs(child_program, exclude_ids)
    return grouped_ids


programs = {}
for noted_program in noted_programs:
    noted_program_data = noted_program.split(' <-> ')
    noted_program_id = noted_program_data[0]
    noted_program_recipients = noted_program_data[1].split(', ')
    programs[noted_program_id] = noted_program_recipients

number_of_groups = 0
ignored_programs = []
for program in programs:
    if program not in ignored_programs:
        ignored_programs += find_child_programs(program)
        number_of_groups += 1

found_programs = find_child_programs('0')
print(len(found_programs))
print(number_of_groups)
