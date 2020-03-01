from day13.common import *


def run(program):
    computer = Computer([], program)
    while not computer.is_finished:
        computer.run_program()
    return computer


if __name__ == '__main__':
    program = get_input("input.txt")
    computer = run(program)
    tiles = [computer.outputs[i] for i in range(2, len(computer.outputs), 3)]
    n_block_tiles = tiles.count(BLOCK_TILE)
    print("Number of block tiles:", n_block_tiles)
