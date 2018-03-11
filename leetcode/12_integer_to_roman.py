def int_to_roman(num):
    """
    :type num: int
    :rtype: str
    """
    if num <= 0 or num > 3999:
        raise ValueError('input value out of range')

    roman = ['IVX', 'XLC', 'CDM', 'M??']
    combinations = [
        [],
        [0],
        [0, 0],
        [0, 0, 0],
        [0, 1],
        [1],
        [1, 0],
        [1, 0, 0],
        [1, 0, 0, 0],
        [0, 2]
    ]

    result = ''
    for tokens in roman:
        if num == 0:
            break;
        idx = num % 10
        num //= 10
        partial = ''.join(tokens[j] for j in combinations[idx])
        result = partial + result
    return result

assert int_to_roman(1) == 'I'
assert int_to_roman(2) == 'II'
assert int_to_roman(3) == 'III'
assert int_to_roman(4) == 'IV'
assert int_to_roman(5) == 'V'
assert int_to_roman(6) == 'VI'
assert int_to_roman(7) == 'VII'
assert int_to_roman(8) == 'VIII'
assert int_to_roman(9) == 'IX'
assert int_to_roman(10) == 'X'
assert int_to_roman(11) == 'XI'
assert int_to_roman(100) == 'C'
assert int_to_roman(200) == 'CC'
assert int_to_roman(600) == 'DC'
assert int_to_roman(1000) == 'M'
print('All test cases passed')
