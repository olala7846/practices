
def reverse_integer(x):
    is_neg = (x < 0)
    x = abs(x)
    reverse = 0
    while x > 0:
        reverse *= 10
        reverse += x % 10
        x = x // 10

    x = -x if is_neg else x
    if -(2**31) < x < (2*31 -1):
        return x
    else:
        return 0


assert reverse_integer(123) == 321
assert reverse_integer(-123) == -321
assert reverse_integer(7) == 7
assert reverse_integer(100) == 1
assert reverse_integer(-100) == -1
assert reverse_integer(2**32) == 0
assert reverse_integer(2**32-1) != 0
assert reverse_integer(-2**31 -1) == 0
assert reverse_integer(-2**31) != 0

print('All test cases passed')
