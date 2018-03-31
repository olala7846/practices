from collections import deque

def longest_valid_parentheses(s):
    stack = list()
    max_len = 0
    max_idx = None
    match = list()
    l = None
    r = None

    for idx, c in enumerate(s):
        match.append(None)

        if c == '(':
            stack.append(idx)
        else:
            try:
                match_idx = stack.pop()
            except IndexError:
                continue

            match[idx] = match_idx
            if match_idx > 0 and match[match_idx-1] is not None:
                match[idx] = match[match_idx-1]

            l = match[idx]
            r = idx
            new_len = r - l + 1
            if new_len > max_len:
                max_idx = idx
                max_len = new_len

    if max_len == 0:
        return ''
    else:
        return s[max_idx-max_len+1:max_idx+1]


test = longest_valid_parentheses

assert test("()") == "()"
assert test("()()") == "()()"
assert test("((()()") == "()()"
assert test("))()()") == "()()"
assert test("()()") == "()()"
assert test("))((") == ""
assert test("((()") == "()"
print("All test passed")
