from day01.common import *


def calculate_fuel_recursive(m):
    return add_fuel(0, m)


def add_fuel(current_fuel, m):
    required_fuel = calculate_fuel(m)
    if required_fuel <= 0:
        return current_fuel
    else:
        return add_fuel(current_fuel + required_fuel, required_fuel)


if __name__ == '__main__':
    summed_fuel = sum(map(calculate_fuel_recursive, get_module_masses()))
    print(summed_fuel)
