"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier,
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""


def check_pandigital(n):
    digits = str(n)
    num_digits = len(digits)
    check_list = list(range(1, num_digits + 1))
    set_list = set([int(i) for i in digits])
    if len(set_list) == num_digits:
        sorted_set_list = sorted(list(set_list))
        for i, ss in enumerate(sorted_set_list):
            if sorted_set_list[i] != check_list[i]:
                return False
        return True
    return False


def get_all_pandigital_numbers(n):
    # TODO: Vectorize the operation - too slow
    ret_list = []
    for i in range(1, n + 1):
        if check_pandigital(i):
            ret_list.append(i)
    return ret_list


if __name__ == "__main__":
    print(get_all_pandigital_numbers(999))
