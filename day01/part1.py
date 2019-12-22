from day01.common import *

if __name__ == '__main__':
    summed_fuel = sum(map(calculate_fuel, get_module_masses()))
    print(summed_fuel)
