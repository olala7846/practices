from collections import deque

def is_valid(s):
    LEFT = set(['(', '[', '{'])
    RIGHT = set([')', ']', '}'])
    COMPLEMENTS = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    stack = deque()

    for c in s:
        if c in LEFT:
            stack.append(c)
        else:
            try:
                p = stack.pop()
            except IndexError:
                return False
            if p != COMPLEMENTS[c]:
                return False
    # make sure nothing is left
    return not stack

assert is_valid('')
assert is_valid('()')
assert is_valid('([]{})')
assert is_valid('{[()]}')
assert is_valid('{[]({([])})}')
assert not is_valid(')')
assert not is_valid('()))}')
assert not is_valid('[}')
assert not is_valid('([][})')
assert not is_valid('[')
assert not is_valid('((')
assert not is_valid('{{{')
print('All tests passed')
