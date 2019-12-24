import sys
import matplotlib.pyplot as plt
from day02.common import get_input
from day11.common import run_robot


def zeros(dimensions):
    array_2d = []
    for y in range(dimensions[1]):
        array_2d.append([])
        for _ in range(dimensions[0]):
            array_2d[y].append(0)
    return array_2d


def get_dimensions(tiles_dict):
    min_x, min_y, max_x, max_y = sys.maxsize, sys.maxsize, -sys.maxsize, -sys.maxsize
    for key in tiles_dict.keys():
        x, y = key
        min_x = min(x, min_x)
        min_y = min(y, min_y)
        max_x = max(x, max_x)
        max_y = max(y, max_y)
    dimensions = (max_x - min_x) + 1, (max_y - min_y) + 1
    return dimensions, min_x, min_y


def dict_to_array(tiles_dict):
    dimensions, min_x, min_y = get_dimensions(tiles_dict)
    array_2d = zeros(dimensions)
    for key, value in tiles_dict.items():
        x, y = key
        x -= min_x
        y -= min_y
        array_2d[y][x] = value
    return array_2d


if __name__ == '__main__':
    program = get_input('input.txt')
    painted_tiles = run_robot(program, 1)
    image = dict_to_array(painted_tiles)
    plt.imshow(image)
    plt.show()
