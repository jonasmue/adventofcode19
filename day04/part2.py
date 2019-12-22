from day04.common import *


def condition3(number_array):
    adjacent = 0
    for i in range(len(number_array) - 1):
        if number_array[i] == number_array[i + 1]:
            adjacent += 1
        elif adjacent == 1:
            return True
        else:
            adjacent = 0
    return adjacent == 1


def check_password(number):
    number_array = number_to_array(number, 6)
    return condition1(number_array) and condition2(number_array) and condition3(number_array)


if __name__ == '__main__':
    password_count = 0
    for i in range(147981, 691423):
        if check_password(i):
            password_count += 1
    print(password_count)
