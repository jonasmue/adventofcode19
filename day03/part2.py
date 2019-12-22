from day03.common import *


def get_distances(coords, intersections):
    intersection_steps = {}
    for step, coordinate in enumerate(coords):
        if coordinate in intersections:
            index = intersections.index(coordinate)
            if index in intersection_steps.keys():
                continue
            intersection_steps[index] = step + 1  # Since step is 0-based

    return [intersection_steps[key] for key in sorted(intersection_steps.keys(), reverse=True)]


if __name__ == '__main__':
    cables = get_input('input.txt')
    intersections, cable_1_coords, cable_2_coords = get_intersections(cables)
    cable_1_distances = get_distances(cable_1_coords, list(intersections))
    cable_2_distances = get_distances(cable_2_coords, list(intersections))
    total_distances = [cable_1_distances[i] + cable_2_distances[i] for i in range(len(cable_1_distances))]
    print(min(total_distances))
