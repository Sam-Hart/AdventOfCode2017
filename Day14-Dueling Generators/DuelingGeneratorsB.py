import os
import sys

COMPARE_PAIRS = 5000000
GENERATOR_A_FACTOR = 16807
GENERATOR_B_FACTOR = 48271
challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

challenge_data = challenge_data.split('\n')


class DuelingGenerator():
    def __init__(self, factor, worthy_multiple=1):
        self.worthy_multiple = worthy_multiple
        self.divisor = 2147483647
        self.factor = factor

    def calculate(self, old_value):
        new_calculation = (old_value * self.factor) % self.divisor
        if new_calculation % self.worthy_multiple != 0:
            new_calculation = self.calculate(new_calculation)
        return new_calculation


class Judge():
    def __init__(self, pairs, gen_a, gen_b):
        self.number_of_pairs = pairs
        self.pairs_matching_in_lower_sixteen_bits = 0
        self.generator_a = gen_a
        self.generator_b = gen_b

    def consider_pairs(self):
        gen_a_result = int(challenge_data[0].split('with ')[1])
        gen_b_result = int(challenge_data[1].split('with ')[1])
        for _ in range(0, self.number_of_pairs):
            gen_a_result = self.generator_a.calculate(gen_a_result)
            gen_b_result = self.generator_b.calculate(gen_b_result)
            bit_len: int
            if gen_a_result.bit_length() > gen_b_result.bit_length():
                bit_len = gen_a_result.bit_length()
            else:
                bit_len = gen_b_result.bit_length()

            gen_a_bytes = gen_a_result.to_bytes(
                (bit_len // 8) + 1,
                'little'
            )
            gen_b_bytes = gen_b_result.to_bytes(
                (gen_b_result.bit_length() // 8) + 1,
                'little'
            )
            if gen_a_bytes[:2] == gen_b_bytes[:2]:
                self.pairs_matching_in_lower_sixteen_bits += 1


generator_a = DuelingGenerator(GENERATOR_A_FACTOR, 4)
generator_b = DuelingGenerator(GENERATOR_B_FACTOR, 8)

judge = Judge(COMPARE_PAIRS, generator_a, generator_b)
judge.consider_pairs()
print(judge.pairs_matching_in_lower_sixteen_bits)
