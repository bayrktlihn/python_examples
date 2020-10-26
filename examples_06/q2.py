# -*- coding: utf-8 -*-

def gcd(num1, num2):
    assert isinstance(num1, int)
    assert isinstance(num2, int)

    divide = 2
    result = 1

    while num1 != 1 or num2 != 1:
        if num1 % divide == 0 and num2 % divide == 0:
            result *= divide
            num1 //= divide
            num2 //= divide
            divide -= 1
        elif num1 % divide == 0:
            num1 //= divide
            divide -= 1
        elif num2 % divide == 0:
            num2 //= divide
            divide -= 1

        divide += 1
    return result


if __name__ == "__main__":
    print(gcd(15, 10))
