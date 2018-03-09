
def longest_palindrom(s):
    max_len = 0
    max_range = None

    # odd
    for i in xrange(len(s)):
        l, r = i, i
        while 0 <= l and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        if max_len < (r - l - 1):
            max_len = (r - l - 1)
            max_range = (l+1, r-1)

    # even
    for i in xrange(1, len(s)):
        l, r = i - 1, i
        while 0 <= l and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        if max_len < (r - l - 1):
            max_len = (r - l - 1)
            max_range = (l+1, r-1)

    return s[max_range[0]: max_range[1] + 1]


assert longest_palindrom('babcc') == 'bab'
assert longest_palindrom('b') == 'b'
assert longest_palindrom('cbabcc') == 'cbabc'
assert longest_palindrom('aabbac') == 'abba'
print('All test cases passed')
