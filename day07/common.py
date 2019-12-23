from itertools import permutations
from day05.common import Computer


def run_computer(computer, last_output):
    computer.inputs.append(last_output)
    computer.run_program()
    return computer.is_finished, computer.outputs[-1]


def run_permutations(l, perm_list):
    perm = permutations(perm_list)
    max_output = 0
    for p in perm:
        computer_pointer = -1
        last_output = 0
        finished = False
        computers = [Computer([input_id], list(l)) for input_id in p]
        while not finished or computer_pointer < len(perm_list) - 1:
            computer_pointer += 1
            computer_pointer %= len(perm_list)
            current_computer = computers[computer_pointer]
            finished, last_output = run_computer(current_computer, last_output)
        max_output = max(max_output, last_output)
    return max_output
