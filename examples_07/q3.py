# -*- coding: utf-8 -*-


def tokenize(haystack: str, min_allowed_length=3):
    return [word for word in get_words(haystack) if len(word) > (min_allowed_length - 1)]


def get_words(text):
    words = []
    current_word = ""

    before_letter = " "

    for letter in text:
        if not before_letter.isalpha() and letter.isalpha():
            current_word = letter
        elif before_letter.isalpha() and letter.isalpha():
            current_word += letter
        elif before_letter.isalpha() and not letter.isalpha():
            words.append(current_word)
            current_word = ""
        before_letter = letter

    if len(current_word) > 0:
        words.append(current_word)

    return words


words = tokenize("alihan/merve aa bayraktar/test example //// example ssss", 3)

print(words)
