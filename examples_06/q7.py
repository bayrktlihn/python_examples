# -*- coding: utf-8 -*-

def is_valid_identification_number(val: str):
    assert isinstance(val, str)

    try:
        val = int(val)
        if 100000000000 > val > 9999999999:
            odd_sum_result = sum_odd_numbers(val)
            even_sum_result = sum_even_numbers(val)

            result = odd_sum_result * 7 - even_sum_result

            ten_digit = get_ten_index(val)
            last_digit = get_last_digit(val)
            sum_without_last_digit = sum_digits_without_last_digit(val)

            if result % 10 == ten_digit and last_digit == sum_without_last_digit % 10:
                return True
        return False


    except ValueError as e:
        return False


def sum_odd_numbers(val):
    val //= 100
    odd_sum_result = 0

    while val > 0:
        odd_sum_result += val % 10
        val = val // 100

    return odd_sum_result


def sum_even_numbers(val):
    odd_sum_result = 0
    val //= 1000

    while val > 0:
        odd_sum_result += val % 10
        val = val // 100

    return odd_sum_result


def get_ten_index(val):
    val_str = str(val)

    return int(val_str[9])


def get_last_digit(val):
    val_str = str(val)
    return int(val_str[10])


def sum_digits_without_last_digit(val):
    val //= 10

    result = 0
    while val > 0:
        result += val % 10
        val //= 10

    return result


if __name__ == "__main__":
    result = is_valid_identification_number("50004577612")

    print(result)
