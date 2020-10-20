def gcd(num_one, num_two):
    divide = 2

    result = 1
    while num_one != 1 or num_two != 1:

        if num_one % divide == 0 and num_two % divide == 0:
            num_one //= divide
            num_two //= divide
            result *= divide
        elif num_one % divide == 0:
            num_one //= divide
        elif num_two % divide == 0:
            num_two //= divide

        if num_one % divide == 0 or num_two % divide == 0:
            divide -= 1

        divide += 1

    return result


print(gcd(6, 4))
