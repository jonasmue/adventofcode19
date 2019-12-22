from day04.common import *


def check_password(number):
    number_array = number_to_array(number, 6)
    return condition1(number_array) and condition2(number_array)


if __name__ == '__main__':
    password_count = 0
    for i in range(147981, 691423):
        if check_password(i):
            password_count += 1
    print(password_count)
