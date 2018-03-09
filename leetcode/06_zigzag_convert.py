
def convert(s, num_rows):
    rows = []
    for i in xrange(num_rows):
        rows.append(list())

    idx = 0
    for row_idx in iter_zigzag(num_rows):
        try:
            rows[row_idx].append(s[idx])
            idx += 1
        except IndexError:
            break

    s = ''
    for row in rows:
        s += ''.join(row)
    return s


def iter_zigzag(num_rows):
    if num_rows == 1:
        while True:
            yield 0

    current = 0
    direction = 1
    yield current
    while True:
        if current == (num_rows - 1) and direction == 1:
            direction = -1
        elif current == 0 and direction == -1:
            direction = 1

        current += direction
        yield current


assert convert('ABCDEFG', 3) == 'AEBDFCG'
assert convert('A', 3) == 'A'
assert convert('ABC', 1) == 'ABC'
assert convert('ABCDEFGHIJ', 10) == 'ABCDEFGHIJ'

print('All test cases passed')
