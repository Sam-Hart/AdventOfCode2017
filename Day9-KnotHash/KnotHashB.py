import os
import sys


def calculate_hash(clear_text):
    text_codes = [ord(char) for char in clear_text]
    text_codes += [17, 31, 73, 47, 23]

    number_ring = [i for i in range(0, 256)]
    ring_position = 0
    skip_size = 0
    for _ in range(0, 64):
        for text_code in text_codes:
            reverse_integers = \
                [i for i in range(ring_position, (ring_position + text_code))]
            elements_to_reverse = \
                [j % len(number_ring) for j in reverse_integers]
            ring_position = (ring_position + text_code + skip_size) \
                % (len(number_ring))

            for reverse_element_index in range(0, len(elements_to_reverse) // 2):
                former_index = elements_to_reverse[reverse_element_index]
                latter_index = elements_to_reverse[-1 * (reverse_element_index + 1)]
                former_number = number_ring[former_index]
                latter_number = number_ring[latter_index]
                number_ring[former_index] = latter_number
                number_ring[latter_index] = former_number
            skip_size += 1

    return number_ring


challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'testInput.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

clear_inputs = [clear_input for clear_input in challenge_data.split('\n')]

for clear_input in clear_inputs:
    hash_output = calculate_hash(clear_input)
    hash_string = ""
    for hash_value in hash_output:
        hash_string += chr(hash_value)
    print(hash_string)