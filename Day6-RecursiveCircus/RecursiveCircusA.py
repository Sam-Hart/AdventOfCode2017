import os
import sys


class Program():
    def __init__(self, name, weight=0, p=None, sub_programs=[]):
        self.name = name
        self.parent = p
        self.sub_programs = sub_programs
        self.weight = weight

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return self.name == str(other)


challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

program_structures = challenge_data.split('\n')
programs = []

for program_structure in program_structures:
    structure = program_structure.split(' -> ')
    program = structure[0].split(' ')
    program_name = program[0]
    program_weight = int(program[1].replace('(', "").replace(')', ""))
    sub_programs = []
    if len(structure) > 1:
        sub_programs += structure[1].split(', ')

    programs.append(
        Program(
            program_name,
            program_weight,
            sub_programs=sub_programs
        )
    )

child_programs = []
for program in programs:
    if not program.sub_programs:
        continue
    for sub_program in program.sub_programs:
        child_programs.append(programs[programs.index(sub_program)])

parent_programs = [
    program for program in programs if program not in child_programs
]
print(parent_programs[0].name)