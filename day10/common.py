import math
from collections import defaultdict


class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + '|' + str(self.y) + ')'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y

    def __hash__(self):
        return hash((self.x, self.y))

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        norm_x = int(self.x * 1000000 / self.magnitude()) / 1000000
        norm_y = int(self.y * 1000000 / self.magnitude()) / 1000000
        return Vector(norm_x, norm_y)


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


def get_input(file_name):
    with open(file_name, 'r') as f:
        asteroids = []
        for y, line in enumerate(f.readlines()):
            for x, character in enumerate(line):
                if character == '#':
                    asteroids.append(Vector(x, y))

        return asteroids
