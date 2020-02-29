from day12.common import *

if __name__ == '__main__':
    moons = get_input('input.txt')
    simulate_motion(moons)
    print(calculate_system_energy(moons))
