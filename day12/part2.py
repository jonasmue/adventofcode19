from day12.common import *
import numpy as np


def build_position_matrix(moons):
    matrix = np.zeros([len(moons), 3])
    for i, m in enumerate(moons):
        matrix[i] = np.array(m.position.as_list())
    return matrix


def efficient_update_velocity(position_matrix, velocity_matrix, gravity_matrix):
    sorted_indices = np.argsort(position_matrix.argsort(axis=0), axis=0)
    sorted_gravities = -np.take_along_axis(gravity_matrix, sorted_indices, 0)
    print("Hej!")


def efficient_update_position(position_matrix, velocity_matrix):
    pass


def efficient_time_step(position_matrix, velocity_matrix, gravity_matrix):
    efficient_update_velocity(position_matrix, velocity_matrix, gravity_matrix)
    efficient_update_position(moons)


if __name__ == '__main__':
    moons = get_input('input.txt')
    n_moons = len(moons)
    velocity_matrix = np.zeros([n_moons, 3])
    position_matrix = build_position_matrix(moons)
    gravity_matrix = np.array(
        [np.array([(n_moons - (i + 1) - ((i + 1) - n_moons)) - (n_moons - 1) for i in range(n_moons)]) for _ in
         range(3)]).T
    initial_positions = position_matrix.copy()
    while True:
        efficient_time_step(position_matrix, velocity_matrix, gravity_matrix)
    print("Done")
