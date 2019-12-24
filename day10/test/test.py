import unittest
from day10.common import *
from day10.part1 import calculate_max_asteroid
from day10.part2 import get_nth_vaporized_asteroid


class TestPart1(unittest.TestCase):
    def test1(self):
        asteroids = get_input('test1.txt')
        correct_point = Vector(5, 8)
        correct_n = 33
        n, p = calculate_max_asteroid(asteroids)
        self.assertEqual(correct_n, n)
        self.assertEqual(correct_point, p)

    def test2(self):
        asteroids = get_input('test2.txt')
        correct_point = Vector(1, 2)
        correct_n = 35
        n, p = calculate_max_asteroid(asteroids)
        self.assertEqual(correct_n, n)
        self.assertEqual(correct_point, p)

    def test3(self):
        asteroids = get_input('test3.txt')
        correct_point = Vector(6, 3)
        correct_n = 41
        n, p = calculate_max_asteroid(asteroids)
        self.assertEqual(correct_n, n)
        self.assertEqual(correct_point, p)

    def test4(self):
        asteroids = get_input('test4.txt')
        correct_point = Vector(11, 13)
        correct_n = 210
        n, p = calculate_max_asteroid(asteroids)
        self.assertEqual(correct_n, n)
        self.assertEqual(correct_point, p)


class TestPart2(unittest.TestCase):
    def test1(self):
        asteroids = get_input('test4.txt')
        correct_point = Vector(8, 2)
        _, p = calculate_max_asteroid(asteroids)
        actual_point = get_nth_vaporized_asteroid(asteroids, p)
        self.assertEqual(correct_point, actual_point)


if __name__ == '__main__':
    unittest.main()
