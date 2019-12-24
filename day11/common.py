from collections import defaultdict
from day05.common import Computer

HEADING_UP = 0
HEADING_LEFT = 1
HEADING_DOWN = 2
HEADING_RIGHT = 3


def turn_left(current_status):
    x, y, current_heading = current_status
    new_heading = (current_heading + 1) % 4
    if current_heading == HEADING_UP:
        return x - 1, y, new_heading
    elif current_heading == HEADING_LEFT:
        return x, y + 1, new_heading
    elif current_heading == HEADING_DOWN:
        return x + 1, y, new_heading
    elif current_heading == HEADING_RIGHT:
        return x, y - 1, new_heading


def turn_right(current_status):
    x, y, current_heading = current_status
    new_heading = current_heading - 1 if current_heading - 1 >= 0 else 3
    if current_heading == HEADING_UP:
        return x + 1, y, new_heading
    elif current_heading == HEADING_LEFT:
        return x, y - 1, new_heading
    elif current_heading == HEADING_DOWN:
        return x - 1, y, new_heading
    elif current_heading == HEADING_RIGHT:
        return x, y + 1, new_heading


def move(move_key, current_status):
    if move_key == 0:
        return turn_left(current_status)
    elif move_key == 1:
        return turn_right(current_status)


def run_robot(program, starting_panel=0):
    tiles = defaultdict(int)
    current_x = 0
    current_y = 0
    current_heading = HEADING_UP
    computer = Computer([], program)
    tiles[(current_x, current_y)] = starting_panel
    while not computer.is_finished:
        computer.inputs.append(tiles[(current_x, current_y)])
        computer.run_program()
        paint_instruction = computer.outputs[-2]
        move_instruction = computer.outputs[-1]
        tiles[(current_x, current_y)] = paint_instruction
        current_status = (current_x, current_y, current_heading)
        current_x, current_y, current_heading = move(move_instruction, current_status)
    return tiles
