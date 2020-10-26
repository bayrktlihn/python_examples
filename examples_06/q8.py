# -*- coding: utf-8 -*-

def is_list_sorted(the_list):
    assert isinstance(the_list, (list, tuple))

    pre_val = the_list[0]

    for element in the_list:
        if pre_val > element:
            return False
        pre_val = element
    return True


if __name__ == "__main__":
    print(is_list_sorted(["ahmet", "alihan", "deniz", "merve"]))
    print(is_list_sorted((1, 2, 3, 4, 8, 3)))
