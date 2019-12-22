from day02.common import *


if __name__ == '__main__':
    input = get_input('input.txt')
    for noun in range(100):
        for verb in range(100):
            l = list(input)
            replace_positions({1: noun, 2: verb}, l)
            if run_program(l) == 19690720:
                result = 100 * noun + verb
                print(str(result))
                break
