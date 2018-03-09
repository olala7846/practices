from collections import deque

def longest_substring_without_repeating_char(s):
    q = deque([])
    max_len = 0
    seen = set()

    for idx, c in enumerate(s):
        if c in seen:
            while q:
                c_pop = q.popleft()
                seen.remove(c_pop)
                if c_pop == c:
                    break

        q.append(c)
        seen.add(c)
        if max_len < len(q):
            max_len = len(q)

    return max_len


func = longest_substring_without_repeating_char

assert func('abcabcbb') == 3
assert func('bbbbbb') == 1
assert func('pwwkew') == 3
print('All test cases passed')
