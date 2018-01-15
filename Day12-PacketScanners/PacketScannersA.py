import os
import sys


class Firewall():
    def __init__(self, firewall_layer_data):
        self.packet_position = 0
        self.firewall_layers = {}
        self.detected_layers = []
        for firewall_layer in firewall_layer_data:
            new_layer = Firewall_Layer(firewall_layer["depth"])
            self.firewall_layers[firewall_layer["layer_id"]] = new_layer

    def get_last_firewall_id(self):
        highest_id = 0
        for layer_index, firewall_layer in self.firewall_layers.items():
            if layer_index > highest_id:
                highest_id = layer_index
        return highest_id

    def traverse_firewall(self):
        while self.packet_position <= self.get_last_firewall_id():
            self.detect_caught_packet()
            self.advance_scanners()
            self.packet_position += 1

    def advance_scanners(self):
        for _, firewall_layer in self.firewall_layers.items():
            firewall_layer.scanner_move()

    def detect_caught_packet(self):
        position = self.packet_position
        if position not in self.firewall_layers.keys():
            return

        if self.firewall_layers[position].scanner_position == 0:
            self.detected_layers.append(position)

    def get_severity(self):
        severity = 0
        for layer in self.detected_layers:
            severity += self.firewall_layers[layer].depth * layer
        return severity


class Firewall_Layer():
    def __init__(self, depth):
        self.scanner_position = 0
        self.scanner_direction = "increasing"
        self.scanner_moves = {
            "increasing": self.increase_scanner,
            "decreasing": self.decrease_scanner
        }
        self.depth = depth

    def scanner_move(self):

        if self.scanner_position <= 0:
            self.scanner_direction = "increasing"
        elif self.scanner_position >= self.depth - 1:
            self.scanner_direction = "decreasing"
        self.scanner_moves[self.scanner_direction]()

    def increase_scanner(self):
        if not self.scanner_position >= self.depth - 1:
            self.scanner_position += 1

    def decrease_scanner(self):
        if not self.scanner_position <= 0:
            self.scanner_position -= 1


challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

firewall_layer_data = []

for firewall_layer in challenge_data.split('\n'):
    firewall_layer_parsed_data = firewall_layer.split(': ')
    layer_id = int(firewall_layer_parsed_data[0])
    layer_depth = int(firewall_layer_parsed_data[1])
    firewall_layer_data.append(
        {
            "layer_id": layer_id,
            "depth": layer_depth
        }
    )

simulated_firewall = Firewall(firewall_layer_data)
simulated_firewall.traverse_firewall()
print(simulated_firewall.get_severity())
