import math

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1) + 2):
        if n % i == 0:
            return False
    return True


def prime_factorization(n):
    # The largest prime factor of a number is 1 plus the floor of the square root of the number + 1
    # Need to account for the fact that python ranges are exclusive of the max, so add 1 more to the max
    factor_list = []
    for i in range(2, int(math.sqrt(n) + 1) + 2):
        if n % i == 0:
            factor_list.append(i)
    prime_set = set(factor_list)
    ret_set = set()
    for i in list(prime_set):
        if is_prime(i):
            ret_set.add(i)
    return ret_set


if __name__ == "__main__":
    print max(prime_factorization(600851475143))
