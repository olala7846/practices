
def generate_parenthesis(n):
    results = list()
    helper('', n, n, results)
    return results

def helper(state, l, r, results):
    if l > r or l < 0 or r < 0:
        return
    if l == 0 and r == 0:
        results.append(state)
        return

    helper(state + '(', l-1, r, results)
    helper(state + ')', l, r-1, results)


assert generate_parenthesis(3) == [
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()",
]

assert generate_parenthesis(1) == ["()"]
assert generate_parenthesis(2) == ["(())", "()()"]
print('All tests passed')
