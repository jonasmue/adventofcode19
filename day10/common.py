import math


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

    def normalize(self):
        magnitude = math.sqrt(self.x ** 2 + self.y ** 2)
        norm_x = int(self.x * 1000000 / magnitude) / 1000000
        norm_y = int(self.y * 1000000 / magnitude) / 1000000
        return Vector(norm_x, norm_y)


def get_input(file_name):
    with open(file_name, 'r') as f:
        asteroids = []
        for y, line in enumerate(f.readlines()):
            for x, character in enumerate(line):
                if character == '#':
                    asteroids.append(Vector(x, y))

        return asteroids
