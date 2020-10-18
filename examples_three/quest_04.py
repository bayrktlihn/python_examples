def sum_begin_to_end(begin, end):
    total = 0
    if begin > end:
        begin, end = end, begin

    for i in range(begin, end + 1):
        total += i
    return total


print(sum_begin_to_end(5, 3))
