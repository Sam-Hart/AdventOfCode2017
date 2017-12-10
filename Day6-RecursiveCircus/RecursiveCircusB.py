import os
import sys


challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()


class Program():
    def __init__(self, name, weight=0, p=None, sub_programs=[]):
        self.name = name
        self.parent = p
        self.sub_programs = sub_programs
        self.weight = weight
        self.supported_weight = 0

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return self.name == str(other)


def find_root_program(programs):
    for program in programs:
        if program.parent is None:
            return program


def find_weight_correction(program):
    sub_program_weights = {}
    for sub_program in program.sub_programs:
        supported_weight = sub_program.supported_weight
        sub_program_weights[supported_weight] = \
            sub_program_weights.setdefault(supported_weight, [])
        sub_program_weights[supported_weight].append(
            sub_program
        )

    for weight, weight_programs in sub_program_weights.items():
        if len(weight_programs) == 1:
            find_weight_correction(weight_programs[0])


def calculate_total_weight(program):
    program.supported_weight = program.weight
    for sub_program in program.sub_programs:
        program.supported_weight += calculate_total_weight(sub_program)
    return program.supported_weight


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

for program in programs:
    if not program.sub_programs:
        continue
    for index, sub_program in enumerate(program.sub_programs):
        if programs.index(sub_program) >= 0:
            program.sub_programs[index] = programs[programs.index(sub_program)]
            program.sub_programs[index].parent = program

root_program = find_root_program(programs)

calculate_total_weight(root_program)
weight_correction = find_weight_correction(root_program)

print("done")
