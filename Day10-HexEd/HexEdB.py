import os
import sys


class Cube():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.directions = {
            "n": self.move_north,
            "s": self.move_south,
            "ne": self.move_northeast,
            "se": self.move_southeast,
            "nw": self.move_northwest,
            "sw": self.move_southwest
        }

    def distance_from(self, distant_location):
        return max(
            abs(self.x - distant_location.x),
            abs(self.y - distant_location.y),
            abs(self.z - distant_location.z)
        )

    def move_direction(self, direction):
        self.directions[direction]()

    def move(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z

    def move_north(self):
        self.move(0, 1, -1)

    def move_south(self):
        self.move(0, -1, 1)

    def move_southeast(self):
        self.move(1, -1, 0)

    def move_southwest(self):
        self.move(-1, 0, 1)

    def move_northeast(self):
        self.move(1, 0, -1)

    def move_northwest(self):
        self.move(-1, 1, 0)


challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

paths = challenge_data.split('\n')

for path in paths:
    directions = path.split(',')
    origin = Cube(0, 0, 0)
    farthest_distance = 0
    current_location = Cube(0, 0, 0)
    for direction in directions:
        current_location.move_direction(direction)
        distance = current_location.distance_from(origin)
        if distance > farthest_distance:
            farthest_distance = distance
    print(farthest_distance)
