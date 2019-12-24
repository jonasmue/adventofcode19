from sys import maxsize
from day10.common import *


def cosine_sim(v1, v2):
    return dot_product(v1, v2)


def is_right_of(v1, v2):
    dot = dot_product(v1, v2)
    det = v1.x * v2.y - v1.y * v2.x
    angle = math.atan2(det, dot)
    return angle > 0


def dot_product(v1, v2):
    return v1.x * v2.x + v1.y * v2.y


def turn_right(current_vector, vectors):
    closest_sim = 0
    closest_vector = None
    for vec in vectors:
        v = Vector(vec.x, vec.y).normalize()
        if v == current_vector:
            continue
        sim = cosine_sim(current_vector, v)
        if sim > closest_sim and is_right_of(current_vector, v):
            closest_sim = sim
            closest_vector = v
    return closest_vector


def shoot(origin, current_vector, remaining_asteroids):
    shortest_distance = maxsize
    closest_asteroid = None
    for asteroid in remaining_asteroids:
        vec = Vector(asteroid.x - origin.x, asteroid.y - origin.y)
        vec_n = vec.normalize()
        if not vec_n == current_vector:
            continue
        distance = vec.magnitude()
        if distance > shortest_distance:
            continue
        shortest_distance = distance
        closest_asteroid = asteroid
    return closest_asteroid


def get_nth_vaporized_asteroid(asteroids, asteroid_pos, n=200):
    vaporized = 0
    current_vector = Vector(0, -1)
    remaining_asteroids = list(asteroids)
    remaining_asteroids.remove(asteroid_pos)
    vectors = [Vector(a.x - asteroid_pos.x, a.y - asteroid_pos.y) for a in remaining_asteroids]
    vaporized_asteroid = None
    while vaporized < n:
        vaporized_asteroid = shoot(asteroid_pos, current_vector, remaining_asteroids)
        current_vector = turn_right(current_vector, vectors)
        if vaporized_asteroid is not None:
            remaining_asteroids.remove(vaporized_asteroid)
            vaporized += 1
    return vaporized_asteroid


if __name__ == '__main__':
    asteroids = get_input('input.txt')
    _, asteroid_pos = calculate_max_asteroid(asteroids)
    nth_asteroid = get_nth_vaporized_asteroid(asteroids, asteroid_pos)
    print(nth_asteroid.x * 100 + nth_asteroid.y)
