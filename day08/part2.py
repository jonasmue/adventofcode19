import matplotlib.pyplot as plt
from day08.common import *


def get_effective_top_layer(layers):
    effective_top_layer = layers[0]
    for layer in layers[1:]:
        for i, pixel in enumerate(layer):
            if effective_top_layer[i] == 2:
                effective_top_layer[i] = pixel
    return effective_top_layer


def reshape(layer, width, height):
    array = []
    offset = 0
    for _ in range(height):
        array.append(layer[offset:offset + width])
        offset += width
    return array


if __name__ == '__main__':
    input_data = get_input('input.txt')
    layers = parse_layers(input_data, WIDTH, HEIGHT)
    top_layer = get_effective_top_layer(layers)
    image = reshape(top_layer, WIDTH, HEIGHT)
    plt.imshow(image)
    plt.show()
