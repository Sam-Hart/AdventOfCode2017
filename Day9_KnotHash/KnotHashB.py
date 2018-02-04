import os
import sys


def calculate_sparse_hash(ascii_codes):
    ascii_codes += [17, 31, 73, 47, 23]
    number_ring = [i for i in range(0, 256)]
    ring_position = 0
    skip_size = 0
    # Generate sparse hash by performing twisting operation using the input
    # codes 64 times, carrying over ring_position and skip_size each time
    for _ in range(0, 64):
        for ascii_code in ascii_codes:
            reverse_integers = \
                [i for i in range(ring_position, (ring_position + ascii_code))]
            elements_to_reverse = \
                [j % len(number_ring) for j in reverse_integers]
            ring_position = (ring_position + ascii_code + skip_size) \
                % (len(number_ring))
            elements_reverse_midpoint = range(
                0, len(elements_to_reverse) // 2
            )
            for reverse_element_index in elements_reverse_midpoint:
                former_index = elements_to_reverse[reverse_element_index]
                latter_index = elements_to_reverse[
                    -(reverse_element_index + 1)
                ]
                former_number = number_ring[former_index]
                latter_number = number_ring[latter_index]
                number_ring[former_index] = latter_number
                number_ring[latter_index] = former_number
            skip_size += 1
    return number_ring


def calculate_dense_hash(number_ring):
    xored_numbers = []
    numbers_to_xor = number_ring[0:16]
    del number_ring[0:16]
    xor_value = 0
    for xor_number in numbers_to_xor:
        xor_value = xor_value ^ xor_number
    xored_numbers.append(xor_value)
    if len(number_ring) > 0:
        xored_numbers += calculate_dense_hash(number_ring)
    return xored_numbers


def calculate_hash(clear_text):
    text_codes = [ord(char) for char in clear_text]
    sparse_hash = calculate_sparse_hash(text_codes)
    dense_hash = calculate_dense_hash(sparse_hash)
    hash_string = ''
    for decimal_value in dense_hash:
        hash_string += '{0:02x}'.format(decimal_value)
    return hash_string


if __name__ == '__main__':
    challenge_data = None
    data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
    with open(data_file_name, 'r') as data_file:
        challenge_data = data_file.read()
    data_file.close()

    clear_text_inputs = [
        clear_text_input for clear_text_input in challenge_data.split('\n')
    ]

    for clear_text_input in clear_text_inputs:
        hash_output = calculate_hash(clear_text_input)
        print(hash_output)
