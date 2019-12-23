from day02.common import get_input
from day05.common import Computer

if __name__ == '__main__':
    l = get_input('input.txt')
    computer = Computer([2], l)
    computer.run_program()
    print('BOOST Keycode:', computer.outputs[-1])
