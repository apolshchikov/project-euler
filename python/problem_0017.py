"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.

The use of "and" when writing out numbers is in compliance with British usage.
"""

number_map = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
    18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
    80: "eighty", 90: "ninety", 100: "hundred", 1000: "thousand"
}


class Number(object):
    def __init__(self, integer):
        Number.get_components(integer)

    @staticmethod
    def get_string(n):
        num_digits = len(str(n))
        magnitude = 10**(num_digits - 1)
        out_str = ""
        if num_digits > 2:
            out_str += number_map[int(n / magnitude)] + " " + number_map[int(n / (n / magnitude))]
        #elif num_digits > 1:
        #    first_number = int(str(n)[0])*magnitude
        #    out_str += number_map[first_number] + " " + number_map[n % first_number]
        elif n != 0:
            out_str += number_map[int(n)]
        return out_str

    @staticmethod
    def get_components(n):
        num_digits = len(str(n))
        magnitudes = sorted([10**i for i in range(0, num_digits)], reverse=True)
        connections = ["", "-", "and"]
        first_digit = int(str(n)[0]) * (10**(num_digits - 1))
        if n % first_digit >= 20:
            break_up = [int(str(n)[i])*(10**(num_digits - i - 1)) for i in range(0, num_digits)]
        else:
            if num_digits > 1 and n > 20:
                break_up = [first_digit]
                remainder = n % first_digit
                break_up.append(remainder)
            else:
                break_up = [n]

        strings = [Number.get_string(i) for i in break_up]
        strings = [" ".join(k).strip() for k in list(zip(strings, connections[len(break_up):0]))]
        print(strings)
        out_str = " ".join(strings).strip().replace(" ", "").replace("-", "")

        return out_str


if __name__ == "__main__":
    problem_str = ""
    #for i in range(1, 1001):
    #    problem_str += Number.get_components(i)

    print(Number.get_components(115))
