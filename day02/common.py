def get_input(file_name):
    with open(file_name, 'r') as f:
        return [int(item) for item in f.read().split(',')]


def replace_positions(subsitutes, list):
    for index, value in subsitutes.items():
        list[index] = value


def operate(l, start_index, f):
    idx_a = l[start_index + 1]
    idx_b = l[start_index + 2]
    a = l[idx_a]
    b = l[idx_b]
    destination = l[start_index + 3]
    l[destination] = f(a, b)


def run_program(l, start_index=0):
    if len(l) <= start_index or len(l) < start_index + 4:
        return -1
    elif l[start_index] == 99:
        return l[0]
    elif l[start_index] == 1:
        operate(l, start_index, lambda a, b: a + b)
    elif l[start_index] == 2:
        operate(l, start_index, lambda a, b: a * b)

    return run_program(l, start_index + 4)
