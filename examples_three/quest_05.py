def is_prime(num):
    if num < 2:
        return False

    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True


def get_primes_number(num):
    primes_numbers = [2]
    for i in range(3, num + 1, 2):
        if is_prime(i):
            primes_numbers.append(i)

    return primes_numbers


get_primes_number(1000000)
