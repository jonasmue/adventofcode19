WIDTH = 25
HEIGHT = 6


def get_input(file_name):
    with open(file_name, 'r') as f:
        return [int(character) for character in f.read().strip()]


def parse_layers(input_data, width, height):
    pixels_per_layer = width * height
    n_layers = int(len(input_data) / (pixels_per_layer))
    layers = []
    offset = 0
    for layer_number in range(n_layers):
        layers.append(input_data[offset:offset + pixels_per_layer])
        offset += pixels_per_layer
    return layers
