def test_triple(a, b, c):
    test_c_2 = a**2 + b**2
    if test_c_2 == c**2:
        return True
    return False

for a in range(1, 1001):
    for b in range(a, 1001):
        for c in range(b, 1001):
            if a+b+c == 1000 and test_triple(a, b, c):
                print(a*b*c)
