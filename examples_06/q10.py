# -*- coding: utf-8 -*-

def get_positive_divisions(number):
    assert isinstance(number, int)

    if number < 0:
        number = -number

    divisions = [1]

    for division in range(2, number // 2 + 1):
        if number % division == 0:
            divisions.append(division)

    if number != 1:
        divisions.append(number)

    return divisions


def is_perfect_number(number):
    assert isinstance(number, int)
    assert number >= 0

    positive_divisions_without_own = get_positive_divisions(number)
    positive_divisions_without_own.pop()

    return sum(positive_divisions_without_own) == number


if __name__ == "__main__":
    print(is_perfect_number(1))
    print(is_perfect_number(28))
    print(is_perfect_number(496))
    print(is_perfect_number(8128))
