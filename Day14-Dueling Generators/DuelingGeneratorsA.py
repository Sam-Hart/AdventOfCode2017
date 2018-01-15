import os
import sys

COMPARE_PAIRS = 5
GENERATOR_A_FACTOR = 16807
GENERATOR_B_FACTOR = 48271
challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'testInput.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

challenge_data = challenge_data.split('\n')


class DuelingGenerator():
    def __init__(self, factor):
        self.divisor = 2147483647
        self.factor = factor

    def calculate(self, ):
        self.calculated_value = (self.calculated_value * self.factor) \
            % self.divisor


class Judge():
    def __init__(self, pairs, gen_a, gen_b):
        self.number_of_pairs = pairs
        self.pairs_matching_in_lower_sixteen_bits = 0
        self.generator_a = gen_a
        self.generator_b = gen_b

    def consider_pairs(self):
        generator_a_seed = challenge_data[0].split('with ')[1]
        generator_b_seed = challenge_data[1].split('with ')[1]
        for _ in range(0, self.number_of_pairs):
            self.generator_a.calculate()
            self.generator_b.calculate()
            





generator_a = DuelingGenerator(int(generator_a_seed), GENERATOR_A_FACTOR)
generator_b = DuelingGenerator(int(generator_b_seed), GENERATOR_B_FACTOR)

judge = Judge(COMPARE_PAIRS, generator_a, generator_b)
