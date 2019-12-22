from day06.common import *


def get_parents(orbit_dict, node):
    parents = []
    while node in orbit_dict.keys():
        parent = orbit_dict[node]
        parents.append(parent)
        node = parent
    parents.reverse()
    return parents


def find_closest_common_parent(l1, l2):
    closest = None
    for i, item in enumerate(l1):
        if i >= len(l2):
            return closest
        elif l2[i] != item:
            return closest
        closest = item
    return closest


def count_transitions(child, parent, orbit_dict):
    count = 0
    current = child
    while orbit_dict[current] != parent:
        count += 1
        current = orbit_dict[current]
    return count


def count_transfers(orbit_dict, node_1, node_2):
    # Idea: Find closest common parent and count steps there
    node_1_parents = get_parents(orbit_dict, node_1)
    node_2_parents = get_parents(orbit_dict, node_2)
    common_parent = find_closest_common_parent(node_1_parents, node_2_parents)
    return count_transitions(node_1, common_parent, orbit_dict) + count_transitions(node_2, common_parent, orbit_dict)


if __name__ == '__main__':
    orbit_list = get_input('input.txt')
    orbit_dict = build_orbit_dict(orbit_list)
    print(count_transfers(orbit_dict, 'YOU', 'SAN'))
