"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def get_multiples(number, max):
    matches = []
    for i in range(0, max):
        if i % number == 0:
            matches.append(i)
    return matches


if __name__ == "__main__":
    numbers = [3, 5]
    multiples_arr = []
    for i in numbers:
        multiples_arr.extend(get_multiples(i, 1000))
    multiple_set = set(multiples_arr)
    print sum(multiple_set)
