DIGIT_MAP = {
  "2": "abc",
  "3": "def",
  "4": "ghi",
  "5": "jkl",
  "6": "mno",
  "7": "pqrs",
  "8": "tuv",
  "9": "wxyz",
}

def gen_dfs(current_str, digits_left, results):
    if not digits_left:
        results.append(current_str)
        return

    next_digit = digits_left[0]
    for c in DIGIT_MAP[next_digit]:
        gen_dfs(current_str + c, digits_left[1:], results)


def letter_combinations(digits):
    results = []
    if not digits:
        return results

    gen_dfs("", digits, results)
    return results

assert letter_combinations("") == []
assert letter_combinations("2") == ["a", "b", "c"]
assert letter_combinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
print('All test cases passed')
