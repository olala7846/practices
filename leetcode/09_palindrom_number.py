import math


def is_palindrom(x):
    if x < 0:
        return False
    if x == 0:
        return True

    r = 1
    l = mathpow(10, math.floor(math.log10(x)))
    while l > r:
        if ((x // l) % 10) == ((x // r) % 10):
            l /= 10
            r *= 10
        else:
            return False
    return 10

# assert is_palindrom(0)
# assert is_palindrom(5)
assert is_palindrom(121)
assert is_palindrom(4321234)
assert not is_palindrom(-3)
assert not is_palindrom(123432)
assert not is_palindrom(322)
print('All test cases pssed')
