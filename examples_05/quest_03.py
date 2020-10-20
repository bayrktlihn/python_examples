def x1_x2(a, b, c):
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return (None, None)

    if delta == 0:
        result = (-b - delta ** 0.5)
        return (result, result)

    x1 = -b - delta ** 0.5
    x2 = -b + delta ** 0.5

    return (x1, x2)


print(x1_x2(1, 2, 1))
