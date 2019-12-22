import unittest
from day06.part2 import *

class TestCase(unittest.TestCase):
    def test_part2(self):
        orbit_list = get_input('test.txt')
        orbit_dict = build_orbit_dict(orbit_list)
        self.assertEqual(count_transfers(orbit_dict, 'YOU', 'SAN'), 4)


if __name__ == '__main__':
    unittest.main()
