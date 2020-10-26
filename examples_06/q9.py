# -*- coding: utf-8 -*-

def insert(the_list, element):
    index_num = find_index(the_list, element)

    the_list.insert(index_num, element)


def find_index(the_list, element):
    index = 0

    for i in range(0, len(the_list)):
        if the_list[i] > element:
            break
        index += 1
    return index


if __name__ == "__main__":
    the_list = [1, 23, 44]
    insert(the_list, 20)
    insert(the_list, 13)
    insert(the_list, 0)
    insert(the_list, 99)
    insert(the_list, 44)
    insert(the_list, 43)
    print(the_list)
