# -*- coding: utf-8 -*-

def is_valid_identification_number(val: str):
    assert isinstance(val, str)

    try:
        val = int(val)
        return 100000000000 > val > 9999999999
    except ValueError as e:
        return False


if __name__ == "__main__":
    result = is_valid_identification_number("wqeqw")

    print(result)

    result = is_valid_identification_number("900000000000")

    print(result)

    result = is_valid_identification_number("90000000000")

    print(result)
