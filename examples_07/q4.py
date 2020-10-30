# -*- coding: utf-8 -*-

def uniques_only(iterable1):
    assert isinstance(iterable1, (list, tuple))

    result = []

    for item in iterable1:
        if item not in result:
            result.append(item)

    return result
