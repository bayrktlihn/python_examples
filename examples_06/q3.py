# -*- coding: utf-8 -*-

from q2 import gcd


def simplify(num1, num2):
    gcd_result = gcd(num1, num2)

    return num1 // gcd_result, num2 // gcd_result


numerator, denominator = simplify(32, 100)

print(numerator, "/", denominator)
