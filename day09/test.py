import unittest
from day05.common import Computer


class TestPart1(unittest.TestCase):
    def test_1(self):
        l = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
        computer = Computer(None, l)
        computer.run_program()
        self.assertEqual(computer.outputs, l)

    def test_2(self):
        l = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
        computer = Computer(None, l)
        computer.run_program()
        self.assertEqual(len(str(computer.outputs[-1])), 16)

    def test_3(self):
        l = [104, 1125899906842624, 99]
        computer = Computer(None, l)
        computer.run_program()
        self.assertEqual(computer.outputs[-1], 1125899906842624)


if __name__ == '__main__':
    unittest.main()
