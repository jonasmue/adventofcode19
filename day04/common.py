def condition1(number_array):
    for i in range(len(number_array) - 1):
        if number_array[i] == number_array[i + 1]:
            return True
    return False


def condition2(number_array):
    for i in range(len(number_array) - 1):
        if number_array[i] > number_array[i + 1]:
            return False
    return True


def number_to_array(number, length=6):
    return [number % 10 ** i // (10 ** (i - 1)) for i in range(length, 0, -1)]
