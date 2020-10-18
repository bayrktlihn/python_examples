def get_positive_divides(num):
    divides = [1]
    if num < 0:
        num = -num
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            divides.append(i)
    if num != 0:
        divides.append(num)
    return divides


def is_prime(num):
    if num < 0:
        return False
    return len(get_positive_divides(num)) == 2


def find_next_prime(num):
    found = False
    while not found:
        num += 1
        if is_prime(num):
            found = True
    return num


print(find_next_prime(17))


