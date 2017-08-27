"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def collatz_chain(starting):
    chain = []
    index = starting
    while index != 1:
        chain.append(int(index))
        index = collatz(index)
    chain.append(1)
    return chain


if __name__ == "__main__":
    max_chain_size = 1
    max_chain_starting = 1
    for i in range(1, 1000000):
        cc = collatz_chain(i)
        size_cc = len(cc)
        if size_cc >= max_chain_size:
            max_chain_size = size_cc
            max_chain_starting = i

    print(max_chain_size, max_chain_starting)
