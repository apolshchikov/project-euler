"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


def convert_int_to_binary(i):
    return "{0:b}".format(i)


def check_palidrome(i):
    if str(i) == "".join(reversed(list(str(i)))):
        return True
    return False


def get_int_palindromes(end_n):
    palindromes = []
    for i in range(1, end_n):
        if check_palidrome(i):
            palindromes.append(i)
    return palindromes


if __name__ == "__main__":
    int_palindromes = get_int_palindromes(1000000)
    combined_palindromes = []
    for ip in int_palindromes:
        if check_palidrome(convert_int_to_binary(ip)):
            combined_palindromes.append(ip)
    print(sum(combined_palindromes))
