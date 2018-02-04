import os
import sys
from Day9_KnotHash.KnotHashB import calculate_hash

challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()
clear_text_input = challenge_data.split('\n')[0]

bit_count = 0
for i in range(0, 128):
    hash_output = calculate_hash(clear_text_input + '-' + str(i))
    hash_numeric_value = int(hash_output, 16)
    # Brian Kernighan's algorithm to calculate number of set bits in a value
    # Though it is a little destructive to the original value
    while hash_numeric_value:
        # Subtracting a number toggles all of the bits from right to left
        # in a number up to and including the rightmost set bit.
        # Performing a bitwise AND after the subtraction with the initial value
        # then unsets the rightmost value. Doing this until the value is 0
        # means that we'll iterate the number of set bits in the number
        hash_numeric_value &= (hash_numeric_value - 1)
        bit_count += 1

print(bit_count)
