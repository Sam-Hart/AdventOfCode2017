import os
import sys


class Firewall():
    def __init__(self, firewall_layer_data):
        self.firewall_layers = {}
        for firewall_layer in firewall_layer_data:
            new_layer = Firewall_Layer(firewall_layer["depth"])
            self.firewall_layers[int(firewall_layer["layer_id"])] = new_layer

    def calculate_delay(self):
        caught = True
        undetected_delay = 0
        calculation_layers = self.firewall_layers
        while caught:
            incremented_firewall_layers = {}
            for layer_index, layer in calculation_layers.items():
                if layer_index % layer.get_scanner_cycle() == 0:
                    for layer_index, layer in calculation_layers.items():
                        incremented_firewall_layers[layer_index + 1] = layer
                    undetected_delay += 1
                    caught = True
                    break
                caught = False
            calculation_layers = incremented_firewall_layers
        return undetected_delay


class Firewall_Layer():
    def __init__(self, depth):
        self.depth = depth

    def get_scanner_cycle(self):
        return (2 * self.depth) - 2


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
    firewall_layer_data.append(
        {
            "layer_id": layer_id,
            "depth": layer_depth
        }
    )

simulated_firewall = Firewall(firewall_layer_data)
print(simulated_firewall.calculate_delay())
