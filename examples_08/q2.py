# -*- coding: utf-8 -*-

from random import shuffle


def letters_replace(text, kv_letters):
    result = ""

    for letter in text:
        if letter.isalpha():
            result += kv_letters[letter]
        else:
            result += letter

    return result


def print_key_value(kv_letters):
    print("key value dict")
    for key, value in kv_letters.items():
        print(key, value)


def key_value_letters() -> dict:
    letters = "abcdefghijklmnopqrstuvwxyz"
    key_letters = [letter for letter in letters]
    value_letters = [letter for letter in letters]
    shuffle(value_letters)

    key_value = {}

    for i in range(len(key_letters)):
        key_value[key_letters[i]] = value_letters[i]

    return key_value


def convert_value_key_letters(kv_letters: dict):
    return {value: key for key, value in kv_letters.items()}


kv_letters = key_value_letters()
print_key_value(kv_letters)

vk_letters = convert_value_key_letters(kv_letters)
print_key_value(vk_letters)

text = """
my name is alihan. i am a worker in siemens. my age is twenty five. i am a computer engineer. i have two sister. i do not have a brother.
my father job is a soldier. my mother job is a homewife.
""".strip()

result = letters_replace(text, kv_letters)

file = open("alihan_bayraktar_sifreleyici.txt", "w", encoding="utf8")
file.write(result)
file.close()

result = letters_replace(result, vk_letters)

file = open("alihan_bayraktar_sifre_kirici.txt", "w", encoding="utf8")
file.write(text)
file.close()
