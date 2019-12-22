from itertools import permutations
from day05.common import Computer
from day02.common import get_input


def run_permutations(l):
    perm = permutations([0, 1, 2, 3, 4])
    max_output = 0
    for p in perm:
        last_output = 0
        for input_id in p:
            computer = Computer()
            inputs = (input_id, last_output)
            computer.run_program(list(l), inputs)
            last_output = computer.outputs[-1]
            if input_id == p[-1]:
                max_output = max(max_output, last_output)
    return max_output


if __name__ == '__main__':
    l = get_input('input.txt')
    print('MAXIMUM OUTPUT:', run_permutations(l))
