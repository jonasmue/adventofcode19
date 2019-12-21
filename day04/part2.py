from day04.common import *


# --- Part Two ---
#
# An Elf just remembered one more important detail: the two adjacent matching digits are not part of a
# larger group of matching digits.
#
# Given this additional criterion, but still ignoring the range rule, the following are now true:
#
# 112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
# 123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
# 111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
# How many different passwords within the range given in your puzzle input meet all of the criteria?


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
    number_array = number_to_array(number)
    return condition1(number_array) and condition2(number_array) and condition3(number_array)


if __name__ == '__main__':
    password_count = 0
    for i in range(147981, 691423):
        if check_password(i):
            password_count += 1
    print(password_count)
