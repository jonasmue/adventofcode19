from day13.common import *


def run(program):
    computer = Computer([], program)
    ball_index = 2
    paddle_index = 2
    while not computer.is_finished:
        computer.run_program()
        for i in range(ball_index, len(computer.outputs), 3):
            if computer.outputs[i] == BALL_TILE:
                ball_index = i
            if computer.outputs[i] == HORIZONTAL_PADDLE_TILE:
                paddle_index = i
        x_pos_ball = computer.outputs[ball_index - 2]
        x_pos_paddle = computer.outputs[paddle_index - 2]
        joystick_input = 1 if x_pos_ball > x_pos_paddle else -1 if x_pos_ball < x_pos_paddle else 0
        computer.inputs.append(joystick_input)
    return computer.outputs[-1]


if __name__ == '__main__':
    program = get_input("input.txt")
    program[0] = 2
    highscore = run(program)
    print("Highscore:", highscore)
