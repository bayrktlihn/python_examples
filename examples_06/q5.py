# -*- coding: utf-8 -*-

from random import randint
from random import shuffle

from q4 import is_strong_password


def generate_strong_password():
    digit_chars = str(randint(10, 9999))
    punctuation_chars = generate_punctuation_chars()
    upper_chars = generate_upper_chars()
    lower_chars = generate_lower_chars()

    result = digit_chars + punctuation_chars + upper_chars + lower_chars
    result_list = list(result)

    shuffle(result_list)

    result = "".join(result_list)

    return result


def generate_upper_chars():
    alphabet = "".join([chr(letter_ord) for letter_ord in range(ord('A'), ord('Z') + 1)])
    alphabet_len = len(alphabet)
    random_len = randint(2, 10)

    result = ""
    for i in range(0, random_len):
        result += alphabet[randint(0, alphabet_len - 1)]

    return result


def generate_lower_chars():
    alphabet = "".join([chr(letter_ord) for letter_ord in range(ord('a'), ord('z') + 1)])
    alphabet_len = len(alphabet)
    random_len = randint(3, 10)

    result = ""
    for i in range(0, random_len):
        result += alphabet[randint(0, alphabet_len - 1)]

    return result


def generate_punctuation_chars():
    punctuation_chars = ".,;:-_?!#*[](){}'\"\\$%&@"
    random_len = randint(1, 10)

    result = ""
    for i in range(0, random_len):
        result += punctuation_chars[randint(0, len(punctuation_chars) - 1)]

    return result


if __name__ == "__main__":
    for i in range(0, 20):
        password = generate_strong_password()
        print(password)
        print(is_strong_password(password))
        print()
