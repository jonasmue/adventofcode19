from day03.common import *

if __name__ == '__main__':
    cables = get_input('input.txt')
    intersections, _, _ = get_intersections(cables)
    distances = [abs(i[0]) + abs(i[1]) for i in intersections]
    print(min(distances))
