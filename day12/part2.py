from day12.common import *


def get_x_positions(moons):
    return [m.position.x for m in moons]


def get_y_positions(moons):
    return [m.position.y for m in moons]


def get_z_positions(moons):
    return [m.position.z for m in moons]


def greatest_common_divisor(a, b):
    assert (a > 0 and b > 0)
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def least_common_multiple(a, b):
    return a * b / greatest_common_divisor(a, b)


def check_x_positions(moons, init_x):
    for i, m in enumerate(moons):
        if m.position.x != init_x[i]:
            return False
        if m.velocity.x != 0:
            return False
    return True


def check_y_positions(moons, init_y):
    for i, m in enumerate(moons):
        if m.position.y != init_y[i]:
            return False
        if m.velocity.y != 0:
            return False
    return True


def check_z_positions(moons, init_z):
    for i, m in enumerate(moons):
        if m.position.z != init_z[i]:
            return False
        if m.velocity.z != 0:
            return False
    return True


if __name__ == '__main__':
    moons = get_input('input.txt')
    n_steps = 0
    init_x = get_x_positions(moons)
    init_y = get_y_positions(moons)
    init_z = get_z_positions(moons)
    x_cycle_time = 0
    y_cycle_time = 0
    z_cycle_time = 0
    while True:
        time_step(moons)
        n_steps += 1
        if check_x_positions(moons, init_x) and not x_cycle_time:
            x_cycle_time = n_steps
        if check_y_positions(moons, init_y) and not y_cycle_time:
            y_cycle_time = n_steps
        if check_z_positions(moons, init_z) and not z_cycle_time:
            z_cycle_time = n_steps
        if x_cycle_time and y_cycle_time and z_cycle_time:
            break

    print(least_common_multiple(least_common_multiple(x_cycle_time, y_cycle_time), z_cycle_time))
