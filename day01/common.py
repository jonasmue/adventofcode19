def calculate_fuel(module_mass):
    return module_mass // 3 - 2


def read_input(file_name):
    with open(file_name, 'r') as f:
        return [int(line) for line in f.readlines()]


def get_module_masses():
    return read_input('input.txt')
