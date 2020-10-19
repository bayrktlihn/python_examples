def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, (num // 2) + 1, 2):
            if num % i == 0:
                return False
    return True


def find_next_prime(num):
    found = False
    while not found:
        num += 1
        if is_prime(num):
            found = True
    return num


print(find_next_prime(17))


