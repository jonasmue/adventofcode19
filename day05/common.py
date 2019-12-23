from collections import defaultdict
from day04.common import number_to_array


class Computer():

    def __init__(self, inputs, program):
        self.outputs = []
        self.inputs = inputs
        self.input_pointer = 0
        self.pointer = 0
        self.relative_base = 0
        self.is_finished = False
        self.init_program(program)

    def init_program(self, program):
        self.program = defaultdict(int)
        for i, item in enumerate(program):
            self.program[i] = item

    def get_read_value(self, mode, index):
        if mode == 0:
            return self.program[index]
        elif mode == 1:
            return index
        elif mode == 2:
            return self.program[self.relative_base + index]

    def get_write_index(self, mode, index):
        if mode == 0:
            return self.program[index]
        elif mode == 1:
            return index
        elif mode == 2:
            return self.program[index] + self.relative_base

    def parse_opcode(self):
        array = number_to_array(self.program[self.pointer], 5)
        op = array[-1] + array[-2] * 10
        mode_1 = array[-3]
        mode_2 = array[-4]
        mode_3 = array[-5]
        return op, mode_1, mode_2, mode_3

    def operate(self, f, mode_1=0, mode_2=0, mode_3=0):
        idx_a = self.program[self.pointer + 1]
        idx_b = self.program[self.pointer + 2]
        a = self.get_read_value(mode_1, idx_a)
        b = self.get_read_value(mode_2, idx_b)
        destination = self.get_write_index(mode_3, self.pointer + 3)
        self.program[destination] = f(a, b)
        self.pointer += 4

    def operate_output(self, mode_1):
        idx = self.program[self.pointer + 1]
        value = self.get_read_value(mode_1, idx)
        self.outputs.append(value)
        print(value)
        self.pointer += 2

    def operate_jump(self, mode_1, mode_2, if_true):
        idx_flag = self.program[self.pointer + 1]
        idx_destination = self.program[self.pointer + 2]
        flag = self.get_read_value(mode_1, idx_flag)
        destination = self.get_read_value(mode_2, idx_destination)
        if (if_true and flag) or (not if_true and not flag):
            self.pointer = destination
        else:
            self.pointer += 3

    def operate_input(self, mode_1):
        destination = self.get_write_index(mode_1, self.pointer + 1)
        self.program[destination] = self.inputs[self.input_pointer]
        self.input_pointer += 1
        self.pointer += 2

    def operate_relative_pointer(self, mode_1):
        idx = self.program[self.pointer + 1]
        self.relative_base += self.get_read_value(mode_1, idx)
        self.pointer += 2

    def run_program(self):
        while True:
            if len(self.program) <= self.pointer:
                return

            op, mode_1, mode_2, mode_3 = self.parse_opcode()

            if op == 99:
                self.is_finished = True
                return
            elif op == 1:
                self.operate(lambda a, b: a + b, mode_1, mode_2, mode_3)
            elif op == 2:
                self.operate(lambda a, b: a * b, mode_1, mode_2, mode_3)
            elif op == 3:
                if self.input_pointer >= len(self.inputs):
                    return
                self.operate_input(mode_1)
            elif op == 4:
                self.operate_output(mode_1)
            elif op == 5:
                self.operate_jump(mode_1, mode_2, True)
            elif op == 6:
                self.operate_jump(mode_1, mode_2, False)
            elif op == 7:
                self.operate(lambda a, b: int(a < b), mode_1, mode_2, mode_3)
            elif op == 8:
                self.operate(lambda a, b: int(a == b), mode_1, mode_2, mode_3)
            elif op == 9:
                self.operate_relative_pointer(mode_1)
