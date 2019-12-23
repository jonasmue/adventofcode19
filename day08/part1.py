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


if __name__ == '__main__':
    input_data = get_input('input.txt')
    layers = parse_layers(input_data, 25, 6)
    zeros = {}
    ones = {}
    twos = {}
    for i, layer in enumerate(layers):
        zeros[i] = layer.count(0)
        ones[i] = layer.count(1)
        twos[i] = layer.count(2)

    zero_min_layer = min(zeros, key=zeros.get)
    print(ones[zero_min_layer] * twos[zero_min_layer])
