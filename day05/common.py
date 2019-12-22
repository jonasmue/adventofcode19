from day02.common import operate
from day04.common import number_to_array


def parse_opcode(opcode):
    array = number_to_array(opcode, 5)
    op = array[-1] + array[-2] * 10
    mode_1 = array[-3]
    mode_2 = array[-4]
    mode_3 = array[-5]
    return op, mode_1, mode_2, mode_3


def operate_save(l, pointer, mode_1, input):
    destination = pointer + 1 if mode_1 else l[pointer + 1]
    l[destination] = input
    return pointer + 2


def operate_output(l, pointer, mode_1):
    idx_a = l[pointer + 1]
    a = idx_a if mode_1 else l[idx_a]
    print(a)
    return pointer + 2


def jump(l, pointer, mode_1, mode_2, if_true):
    idx_a = l[pointer + 1]
    idx_b = l[pointer + 2]
    a = idx_a if mode_1 else l[idx_a]
    b = idx_b if mode_2 else l[idx_b]
    if if_true:
        return b if a else pointer + 3
    else:
        return pointer + 3 if a else b


def run_program(l, input_id, pointer=0):
    if len(l) <= pointer:
        return

    op, mode_1, mode_2, mode_3 = parse_opcode(l[pointer])
    if op == 99:
        return
    elif op == 1:
        pointer = operate(l, pointer, lambda a, b: a + b, mode_1, mode_2, mode_3)
    elif op == 2:
        pointer = operate(l, pointer, lambda a, b: a * b, mode_1, mode_2, mode_3)
    elif op == 3:
        pointer = operate_save(l, pointer, mode_1, input_id)
    elif op == 4:
        pointer = operate_output(l, pointer, mode_1)
    elif op == 5:
        pointer = jump(l, pointer, mode_1, mode_2, True)
    elif op == 6:
        pointer = jump(l, pointer, mode_1, mode_2, False)
    elif op == 7:
        pointer = operate(l, pointer, lambda a, b: int(a < b), mode_1, mode_2, mode_3)
    elif op == 8:
        pointer = operate(l, pointer, lambda a, b: int(a == b), mode_1, mode_2, mode_3)

    return run_program(l, input_id, pointer)
