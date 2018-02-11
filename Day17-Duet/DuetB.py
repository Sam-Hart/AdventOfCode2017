import os
import sys
from collections import deque


class Program():
    def __init__(self, program_id, instructions):
        self.program_id = program_id
        self.line = 0
        self.send_deque = deque()
        self.receive_deque = None
        self.instructions = instructions
        self.sent_times = 0
        self.registers = {
            'p': self.program_id
        }
        self.commands = {
            'snd': self.send_value,
            'set': self.set_register,
            'add': self.add_register,
            'mul': self.multiply_register,
            'mod': self.modulus_register,
            'rcv': self.receive_to_register,
            'jgz': self.instruction_jump_if_not_zero
        }
        self.receiving_register = None
        self.terminated = False

    def execute_next_instruction(self):
        if not self.terminated and not self.receiving_register:
            current_instruction = self.instructions[self.line].split(' ')
            command = current_instruction[0]
            command_arguments = self.extract_arguments(current_instruction[1:])
            self.commands[command](command_arguments)
            self.line += 1
        else:
            return

        if self.line >= len(self.instructions) and not self.terminated:
            self.terminated = True

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

    def send_value(self, command_arguments):
        send_value = 0
        try:
            send_value = int(command_arguments[0])
        except ValueError:
            send_value = self.registers.get(command_arguments[0], 0)
        self.sent_times += 1
        self.send_deque.append(send_value)

    def receive_value(self):
        if len(self.receive_deque) > 0:
            self.registers[self.receiving_register] = \
                self.receive_deque.popleft()
            self.receiving_register = None

    def receive_to_register(self, command_arguments):
        self.receiving_register = command_arguments[0]

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

    def instruction_jump_if_not_zero(self, command_arguments):
        compare_value = 0
        try:
            compare_value = int(command_arguments[0])
        except ValueError:
            compare_value = self.registers.get(command_arguments[0], 0)
        if compare_value > 0:
            self.line += command_arguments[1] - 1


class Tablet():
    def __init__(self, code, number_of_programs):
        self.programs = []
        instructions = code.split('\n')
        for i in range(number_of_programs):
            self.programs.append(Program(i, instructions))

        for i in range(number_of_programs):
            next_program = (i + 1) % len(self.programs)
            # Wire up the receiving deque to be the sending deque of the
            # next program
            self.programs[i].receive_deque = \
                self.programs[next_program].send_deque

    def execute_programs(self):

        while not self.all_halted():
            for program in self.programs:
                program.execute_next_instruction()
            for program in self.programs:
                if program.receiving_register:
                    program.receive_value()
        print(self.programs[1].sent_times)

    def all_halted(self):
        for program in self.programs:
            if not program.receiving_register and not program.terminated:
                return False
        return True

    def all_waiting(self):
        for program in self.programs:
            if not program.receiving_register:
                return False
        return True

    def all_terminated(self):
        for program in self.programs:
            if not program.terminated:
                return False
        return True


challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

gamegear = Tablet(challenge_data, 2)
gamegear.execute_programs()
