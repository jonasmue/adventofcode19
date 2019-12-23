from day02.common import get_input
from day07.common import *

if __name__ == '__main__':
    l = get_input('input.txt')
    print('MAXIMUM OUTPUT:', run_permutations(l, [0, 1, 2, 3, 4]))
