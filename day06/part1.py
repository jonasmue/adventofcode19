from day06.common import *


def count_recursive(orbitee, orbit_dict):
    parent = orbit_dict[orbitee]
    if not parent in orbit_dict.keys():
        return 1
    return 1 + count_recursive(parent, orbit_dict)


def count_orbits(orbit_dict):
    orbit_count = 0
    for orbitee in orbit_dict.keys():
        orbit_count += count_recursive(orbitee, orbit_dict)
    return orbit_count


if __name__ == '__main__':
    orbit_list = get_input('input.txt')
    orbit_dict = build_orbit_dict(orbit_list)
    print(count_orbits(orbit_dict))
