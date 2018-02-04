import os
import sys

challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

reverse_lengths = [int(i) for i in challenge_data.rstrip().split(",")]

number_ring = [i for i in range(0, 256)]
ring_position = 0
skip_size = 0


for reverse_length in reverse_lengths:
    reverse_integers = \
        [i for i in range(ring_position, (ring_position + reverse_length))]
    elements_to_reverse = \
        [j % len(number_ring) for j in reverse_integers]
    ring_position = (ring_position + reverse_length + skip_size) \
        % (len(number_ring))

    for reverse_element_index in range(0, len(elements_to_reverse) // 2):
        former_index = elements_to_reverse[reverse_element_index]
        latter_index = elements_to_reverse[-1 * (reverse_element_index + 1)]
        former_number = number_ring[former_index]
        latter_number = number_ring[latter_index]
        number_ring[former_index] = latter_number
        number_ring[latter_index] = former_number
    skip_size += 1

print(number_ring[0] * number_ring[1])
