import os
import sys
from math import log
from Day9_KnotHash.KnotHashB import calculate_hash

challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()
clear_text_input = challenge_data.split('\n')[0]


def bit_positions(n):
    bit_positions = []
    while n:
        power_of_2 = n & (~n+1)
        bit_positions.append(int(log(power_of_2, 2)))
        n ^= power_of_2
    return bit_positions


class Graph:
    def __init__(self, bit_map):
        self.bmp = bit_map

    def safe_coordinates(self, i, j, visited):
        min_i = max([0, i - 1])
        max_i = min([i + 1, len(self.bmp) - 1])
        min_j = max([0, j - 1])
        max_j = min([j + 1, len(self.bmp[i]) - 1])
        safe_coordinates = []
        for x in range(min_j, max_j + 1):
            for y in range(min_i, max_i + 1):
                diagonal = abs(x - j) == abs(y - i)
                if not diagonal and self.bmp[y][x] is 1 and not visited[y][x]:
                    safe_coordinates.append([x, y])
        return safe_coordinates

    def DFS(self, i, j, visited):

        safe_coordinates = self.safe_coordinates(i, j, visited)
        visited[i][j] = True
        for coord in safe_coordinates:
            self.DFS(coord[1], coord[0], visited)

    def count_regions(self):
        visited = [
            [
                False for j in range(len(self.bmp[i]))
            ]
            for i in range(len(self.bmp))
        ]
        count = 0
        for i in range(len(self.bmp)):
            for j in range(len(self.bmp[i])):
                if not visited[i][j] and self.bmp[i][j] == 1:
                    self.DFS(i, j, visited)
                    count += 1

        return count


bit_map = []

for i in range(0, 128):
    hash_output = calculate_hash(clear_text_input + '-' + str(i))
    binary_hash_output = int(hash_output, 16)
    bit_map.append([0] * 128)
    for bit_position in bit_positions(binary_hash_output):
        bit_map[i][bit_position] = 1

region_graph = Graph(bit_map)
print(region_graph.count_regions())
