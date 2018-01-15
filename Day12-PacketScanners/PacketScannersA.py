import os
import sys


class Firewall():
    def __init__(self, firewall_layer_data):
        self.packet_position = 0
        self.firewall_layers = []
        for firewall_layer in firewall_layer_data:
            new_layer = Firewall_Layer(firewall_layer)
            self.firewall_layers

class Firewall_Layer():
    def __init__(self, firewall_id, depth):
        self.id = firewall_id
        self.depth = depth


challenge_data = None
data_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'testInput.txt')
with open(data_file_name, 'r') as data_file:
    challenge_data = data_file.read()
data_file.close()

firewall_layer_data = []

for firewall_layer in challenge_data.split('\n'):
    firewall_layer_parsed_data = firewall_layer.split(': ')
    layer_id = int(firewall_layer_parsed_data[0])
    layer_depth = int(firewall_layer_parsed_data[1])
    firewall_layer_data.append({layer_id: layer_depth})

simulated_firewall = Firewall(firewall_layer_data)
