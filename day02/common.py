def get_input(file_name):
    with open(file_name, 'r') as f:
        return [int(item) for item in f.read().split(',')]


def replace_positions(subsitutes, list):
    for index, value in subsitutes.items():
        list[index] = value


def operate(l, pointer, f, mode_1=0, mode_2=0, mode_3=0):
    idx_a = l[pointer + 1]
    idx_b = l[pointer + 2]
    destination = pointer + 3 if mode_3 else l[pointer + 3]
    a = idx_a if mode_1 else l[idx_a]
    b = idx_b if mode_2 else l[idx_b]
    l[destination] = f(a, b)
    return pointer + 4


def run_program(l, start_index=0):
    if len(l) <= start_index or len(l) < start_index + 4:
        return -1
    elif l[start_index] == 99:
        return l[0]
    elif l[start_index] == 1:
        start_index = operate(l, start_index, lambda a, b: a + b)
    elif l[start_index] == 2:
        start_index = operate(l, start_index, lambda a, b: a * b)

    return run_program(l, start_index)
