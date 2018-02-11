import os
import sys


class Tablet():
    def __init__(self):
        self.line = 0
        self.registers = {}
        self.commands = {
            'snd': self.play_sound,
            'set': self.set_register,
            'add': self.add_register,
            'mul': self.multiply_register,
            'mod': self.modulus_register,
            'rcv': self.recover_frequency,
            'jgz': self.instruction_jump_if_not_zero
        }
        self.frequency = None

    def extract_arguments(self, provided_arguments):
        extracted_arguments = []
        extracted_arguments.append(provided_arguments.pop(0))
        if len(provided_arguments) > 0:
            value_argument = provided_arguments.pop(0)
            try:
                value_argument = int(value_argument)
            except ValueError:
                value_argument = self.registers.get(value_argument, 0)
            extracted_arguments.append(value_argument)
        return extracted_arguments

    def interpret_program(self, code):
        instructions = code.split('\n')
        while self.line < len(instructions):
            instruction = instructions[self.line].split(' ')
            command = instruction[0]
            command_arguments = self.extract_arguments(instruction[1:])
            self.commands[command](command_arguments)
            self.line += 1

    def play_sound(self, command_arguments):
        lookup_register = command_arguments[0]
        self.frequency = self.registers[lookup_register]

    def set_register(self, command_arguments):
        self.registers[command_arguments[0]] = command_arguments[1]

    def add_register(self, command_arguments):
        self.registers[command_arguments[0]] = \
            self.registers.get(command_arguments[0], 0) + command_arguments[1]

    def multiply_register(self, command_arguments):
        self.registers[command_arguments[0]] = \
            self.registers.get(command_arguments[0], 0) * command_arguments[1]

    def modulus_register(self, command_arguments):
        self.registers[command_arguments[0]] = \
            self.registers.get(command_arguments[0], 0) % command_arguments[1]

    def recover_frequency(self, command_arguments):
        if self.registers[command_arguments[0]] != 0:
            print(self.frequency)

    def instruction_jump_if_not_zero(self, command_arguments):
        if self.registers[command_arguments[0]] != 0:
            self.line += command_arguments[1] - 1


challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

gamegear = Tablet()
gamegear.interpret_program(challenge_data)
