from day04.common import number_to_array


class Computer():

    def __init__(self, inputs, program):
        self.outputs = []
        self.inputs = inputs
        self.input_pointer = 0
        self.program = program
        self.pointer = 0
        self.is_done = False

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
        destination = self.pointer + 3 if mode_3 else self.program[self.pointer + 3]
        a = idx_a if mode_1 else self.program[idx_a]
        b = idx_b if mode_2 else self.program[idx_b]
        self.program[destination] = f(a, b)
        self.pointer += 4

    def operate_output(self, mode_1):
        idx_a = self.program[self.pointer + 1]
        a = idx_a if mode_1 else self.program[idx_a]
        self.outputs.append(a)
        print(a)
        self.pointer += 2

    def operate_jump(self, mode_1, mode_2, if_true):
        idx_a = self.program[self.pointer + 1]
        idx_b = self.program[self.pointer + 2]
        a = idx_a if mode_1 else self.program[idx_a]
        b = idx_b if mode_2 else self.program[idx_b]
        if (if_true and a) or (not (if_true) and not (a)):
            self.pointer = b
        else:
            self.pointer += 3

    def operate_input(self, mode_1):
        destination = self.pointer + 1 if mode_1 else self.program[self.pointer + 1]
        self.program[destination] = self.inputs[self.input_pointer]
        self.input_pointer += 1
        self.pointer += 2

    def run_program(self):

        if len(self.program) <= self.pointer:
            return

        op, mode_1, mode_2, mode_3 = self.parse_opcode()
        if op == 99:
            self.is_done = True
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

        return self.run_program()
