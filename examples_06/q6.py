# -*- coding: utf-8 -*-

def get_color(x, y):
    x_values = "abcdefgh"

    assert isinstance(x, str)
    assert isinstance(y, int)

    assert x in x_values
    assert -1 < y < 9

    x_index = x_values.index(x)
    y_index = y - 1

    # chessboard = get_chessboard()
    #
    # if chessboard[x_index][y_index] == 0:
    #     return "black"
    # return "white"

    result = (x_index + y_index) % 2

    if result == 0:
        return "black"

    return "white"


def get_chessboard():
    # 0 is black 1 is white
    chessboard = []

    for i in range(0, 8):
        chessboard.append([])
        for j in range(0, 8):
            chessboard[i].append((i + j) % 2)
    return chessboard


if __name__ == "__main__":
    print(get_color("a", 1))
    print(get_color("h", 8))
