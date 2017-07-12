"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
# TODO: Use least common multiple approach with prime factorization

def consecutive_factors(n):
    # Finds the smallest number that can be divided by all numbers smaller and inclusive of n
    factors = range(1, n + 1)
    count_values = len(factors)
    found = False
    smallest = 0

    if n == 1:
        index = n
    else:
        index = consecutive_factors(n-1)
    while found is False:
        check_factors = list(set(map(lambda x: index % x == 0, factors)))
        if False not in check_factors:
            smallest = index
            found = True
            break
        index += 1
    return smallest


if __name__ == "__main__":
    print consecutive_factors(10)
