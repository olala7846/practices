# leet code 01 two sum

def two_sum(nums, target):
    seen = dict()
    for idx, n in enumerate(nums):
        if (target - n) in seen:
            return [seen[target - n], idx]
        else:
            seen[n] = idx
    return None

assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([11, 7, 15, 2], 9) == [1, 3]
print('All tests passed')
