from day08.common import *

if __name__ == '__main__':
    input_data = get_input('input.txt')
    layers = parse_layers(input_data, WIDTH, HEIGHT)
    zeros = {}
    ones = {}
    twos = {}
    for i, layer in enumerate(layers):
        zeros[i] = layer.count(0)
        ones[i] = layer.count(1)
        twos[i] = layer.count(2)

    zero_min_layer = min(zeros, key=zeros.get)
    print(ones[zero_min_layer] * twos[zero_min_layer])
