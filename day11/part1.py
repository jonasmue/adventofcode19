from day02.common import get_input
from day11.common import run_robot

if __name__ == '__main__':
    program = get_input('input.txt')
    painted_tiles = run_robot(program)
    print(len(painted_tiles.items()))
