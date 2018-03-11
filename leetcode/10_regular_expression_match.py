from collections import deque


def is_match(s, p):
    search = deque([])
    explored = set()

    def visit(s, p):
        state = (s, p)
        if state not in explored:
            search.append(state)
            explored.add(state)

    visit(s, p)

    while search:
        a_str, a_ptn = search.popleft()
        if not a_ptn:
            if not a_str:
                return True
            else:
                continue

        if len(a_ptn) > 1 and a_ptn[1] == '*':
            visit(a_str, a_ptn[2:])
            if a_str and (a_str[0] == a_ptn[0] or a_ptn[0] == '.'):
                visit(a_str[1:], a_ptn[2:])
                visit(a_str[1:], a_ptn)

        else:
            if a_str and (a_str[0] == a_ptn[0] or a_ptn[0] == '.'):
                visit(a_str[1:], a_ptn[1:])
    return False


assert is_match('aa', 'a*')
assert is_match('c', '.')
assert is_match('cba', '.*')
assert is_match('cbagg', '.*gg')
assert is_match('aaaab', 'a*b')
assert is_match('abcaaab', 'abcaa*b')
print('All test cases passed')
