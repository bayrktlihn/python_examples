# -*- coding: utf-8 -*-

def reverse_lookup(the_dict: dict, searched_value):

    return [key for key, value in the_dict.items() if value == searched_value]


the_dict = {"alihan": 1, "merve" : 1, "deniz" : 1, "ahmet": 2, "ilknur": 2}

print(reverse_lookup(the_dict, 2))
