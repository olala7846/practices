
# The leetcode test cases doesn't make much sense,
# I'll just skip it for now


def atoi(s):
    s = s.strip()
    idx = 0
    is_neg = False
    if s[0] == '-':
        is_neg = True
        idx += 1
    elif s[0] == '+':
        idx += 1

    num = 0
    while idx < len(s):
        num *= 10
        num += (ord(s[idx]) - ord('0'))
        idx += 1

    return num if not is_neg else -num

assert atoi('123') == 123
assert atoi('-123') == -123
assert atoi('0') == 0
assert atoi('   123') == 123
assert atoi('\t123') == 123
assert atoi('+123') == 123
print('All test cases passed')
