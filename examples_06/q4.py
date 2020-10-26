# -*- coding: utf-8 -*-

def is_strong_password(password):
    assert isinstance(password, str)

    password_len = len(password)
    len_digit_result = len_digit(password)
    len_upper_chars_result = len_upper_chars(password)
    len_punctuation_chars_result = len_punctuation_chars(password)

    result = password_len > 7 and len_digit_result > 1
    result = result and len_punctuation_chars_result > 0
    result = result and len_upper_chars_result > 1

    return result


def len_digit(password: str):
    return len([letter for letter in password if letter.isdigit()])
    # result = 0
    #
    # for letter in password:
    #     if letter.isdigit():
    #         result += 1
    # return result


def len_punctuation_chars(password: str):
    punctuation_chars = ".,;:-_?!#*[](){}'\"\\$%&@"
    return len([letter for letter in password if letter in punctuation_chars])
    # result = 0
    #
    # for letter in password:
    #     if letter in punctuation_chars:
    #         result += 1
    # return result


def len_upper_chars(password: str):
    return len([letter for letter in password if letter.isupper()])

    # result = 0
    #
    # for letter in password:
    #     if letter.isupper():
    #         result += 1
    # return result

if __name__ == "__main__":
    my_password = "ALihan61*"
    print(is_strong_password(my_password))
