def roman_to_int(s):
    """
    :type s: str
    :rtype: int
    """
    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    val = 0
    while s:
        if len(s) > 1:
            matched = False
            if s.startswith('IV'):
                val += 4
                matched = True
            elif s.startswith('XL'):
                val += 40
                matched = True
            elif s.startswith('CD'):
                val += 400
                matched = True
            elif s.startswith('IX'):
                val += 9
                matched = True
            elif s.startswith('XC'):
                val += 90
                matched = True
            elif s.startswith('CM'):
                val += 900
                matched = True

            if matched:
                s = s[2:]
                continue

        key = s[0]
        val += mapping[key]
        s = s[1:]
    return val

assert roman_to_int('X') == 10
assert roman_to_int('IV') == 4
assert roman_to_int('MMIV') == 2004
assert roman_to_int('MCMXCVI') == 1996
assert roman_to_int('MCDLXXVI') == 1476
print('All test cases passed')
