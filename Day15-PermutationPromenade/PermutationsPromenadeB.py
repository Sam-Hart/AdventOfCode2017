import os
import sys
from collections import deque

beginning_ord = ord('a')
ending_ord = ord('p')

if beginning_ord > ending_ord:
    ending_ord, beginning_ord = beginning_ord, ending_ord

characters = deque([
    chr(letter_ord) for letter_ord in range(beginning_ord, ending_ord + 1)
])


def spin(instruction_arguments):
    spin_amount = int(instruction_arguments)
    characters.rotate(spin_amount)


def exchange(instruction_arguments):
    a, b = [int(x) for x in instruction_arguments.split('/')]
    characters[a], characters[b] = characters[b], characters[a]


def partner(instruction_arguments):
    a, b = [characters.index(x) for x in instruction_arguments.split('/')]
    characters[a], characters[b] = characters[b], characters[a]


commands = {
    's': spin,
    'x': exchange,
    'p': partner
}


challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

dance_instructions = challenge_data.split(',')

seen = []
for i in range(1000000000):
    s = ''.join(characters)
    if s in seen:
        print(seen[1000000000 % i])
        break
    seen.append(s)
    for instruction in dance_instructions:
        commands[instruction[0]](instruction[1:])
print(''.join(characters))
