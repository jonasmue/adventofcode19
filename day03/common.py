def get_input(file_name):
    with open(file_name, 'r') as f:
        return [line.split(',') for line in f.readlines()]


def parse_instruction(instruction):
    return (instruction[0], int(instruction[1:]))


def get_coords(cable):
    current_x = 0
    current_y = 0
    coords = []
    for instruction in cable:
        direction, amount = parse_instruction(instruction)
        for i in range(amount):
            if direction == 'R':
                current_x += 1
            elif direction == 'L':
                current_x -= 1
            elif direction == 'U':
                current_y += 1
            elif direction == 'D':
                current_y -= 1
            coords.append((current_x, current_y))

    return coords


def get_intersections(cables):
    cable_1_coords = get_coords(cables[0])
    cable_2_coords = get_coords(cables[1])
    return set(cable_1_coords).intersection(set(cable_2_coords)), cable_1_coords, cable_2_coords