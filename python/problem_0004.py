"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def reverse_string(k):
    ret_str = ""
    index = len(k) - 1
    while index >= 0:
        ret_str += k[index]
        index -= 1
    return ret_str


def is_palindrome(n):
    string_n = str(n)
    if string_n == reverse_string(string_n):
        return True
    return False


if __name__ == "__main__":
    max = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            prod = i * j
            if is_palindrome(prod) and prod >= max:
                max = prod
    print max
