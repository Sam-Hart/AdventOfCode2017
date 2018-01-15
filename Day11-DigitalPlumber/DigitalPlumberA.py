import os
import sys

challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

noted_programs = challenge_data.split('\n')


def find_child_programs(program_id, exclude_ids=['0']):
    child_programs = []
    child_programs += programs[program_id]
    for exclude_id in exclude_ids:
        if exclude_id in child_programs:
            child_programs.remove(exclude_id)
    exclude_ids += child_programs
    child_programs_count = len(child_programs)
    for child_program in child_programs:
        child_programs_count += find_child_programs(child_program, exclude_ids)
    return child_programs_count


programs = {}
for noted_program in noted_programs:
    noted_program_data = noted_program.split(' <-> ')
    noted_program_id = noted_program_data[0]
    noted_program_recipients = noted_program_data[1].split(', ')
    programs[noted_program_id] = noted_program_recipients

found_programs = find_child_programs('0')
print(found_programs + 1)  # to account for 0 containing itself
