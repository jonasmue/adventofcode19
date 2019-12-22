from day02.common import *

if __name__ == '__main__':
    l = get_input('input.txt')
    replace_positions({1: 12, 2: 2}, l)
    print(run_program(l))
