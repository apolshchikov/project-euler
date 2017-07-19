from math import sqrt


def compute_triangle_number(n):
    return sum(list(range(1, n + 1)))


def get_factors(n):
    factors = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n / i)
    factors = sorted([int(i) for i in factors])
    return factors


if __name__ == "__main__":
    max_factors = 0
    current_triangle_number = 1
    index = 1

    while max_factors < 500:
        current_triangle_number = compute_triangle_number(index)
        max_factors = len(get_factors(current_triangle_number))
        index += 1

    print(current_triangle_number, max_factors)
