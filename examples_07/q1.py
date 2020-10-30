# -*- coding: utf-8 -*-

import string


def caesar_encryption(number_of_letters_to_scroll, text: str):
    text = text.lower()

    letters = string.ascii_lowercase

    result = ""

    for letter in text:
        if letter.isalpha():
            new_letter = letters[(letters.index(letter) + number_of_letters_to_scroll) % 26]
            result += new_letter
        else:
            result += letter

    return result


print(caesar_encryption(1, "alihan bayraktarz"))
