import os
import sys


def calculate_stream_score(stream):
    nest_level = 0
    total_score = 0
    ignore_next = False
    garbage = False
    cleaned_up_stream = ""
    for i, character in enumerate(stream):
        if ignore_next:
            ignore_next = False
            cleaned_up_stream += character
            continue
        if character == '!':
            ignore_next = True
            cleaned_up_stream += character
        if character == '>':
            garbage = False
            cleaned_up_stream += character
        if garbage:
            continue
        if character == '<':
            garbage = True
            cleaned_up_stream += character
        if character == '{':
            cleaned_up_stream += character
            nest_level += 1
            total_score += nest_level
        if character == '}':
            cleaned_up_stream += character
            nest_level -= 1
        if character == ',':
            cleaned_up_stream += character
    return total_score, len(stream) - len(cleaned_up_stream)


challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()
streams = challenge_data.split('\n')
for stream in streams:
    print(calculate_stream_score(stream))
