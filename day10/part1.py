from collections import defaultdict

from day10.common import *


def calculate_max_asteroid(asteroids):
    visible_asteroids = defaultdict(list)
    max_len = 0
    max_p = None
    for p in asteroids:
        for q in asteroids:
            if p == q:
                continue
            x_diff = q.x - p.x
            y_diff = q.y - p.y
            v = Vector(x_diff, y_diff).normalize()
            if v not in visible_asteroids[p]:
                visible_asteroids[p].append(v)

        n_visible_asteroids = len(visible_asteroids[p])
        if n_visible_asteroids > max_len:
            max_len = n_visible_asteroids
            max_p = p
    return max_len, max_p


if __name__ == '__main__':
    asteroids = get_input('input.txt')
    print(calculate_max_asteroid(asteroids))
