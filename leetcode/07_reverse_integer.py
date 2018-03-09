
def reverse_integer(x):
    is_neg = (x < 0)
    x = abs(x)
    reverse = 0
    while x > 0:
        reverse *= 10
        reverse += x % 10
        x = x // 10

    reverse = -reverse if is_neg else reverse

    if -(2**31) <= reverse <= (2**31 -1):
        return reverse
    else:
        return 0

assert reverse_integer(123) == 321
assert reverse_integer(-123) == -321
assert reverse_integer(7) == 7
assert reverse_integer(100) == 1
assert reverse_integer(-100) == -1
assert reverse_integer(2**31) == 0

num_rev = int(str(2**31)[::-1])
assert reverse_integer(num_rev) == 0

num_rev = int(str(2**31 - 1)[::-1])
assert reverse_integer(num_rev) != 0

print('All test cases passed')
