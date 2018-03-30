
def remove_element(nums, x):
    w_idx = 0
    for val in nums:
        if val == x:
            continue
        else:
            nums[w_idx] = val
            w_idx += 1
    return w_idx

def test(nums, x):
    l = remove_element(nums, x)
    return nums[:l]

assert test([3, 2, 2, 3], 3) == [2, 2]
assert test([], 3) == []
assert test([1, 2, 3], 3) == [1, 2]
assert test([3, 3, 3], 3) == []
print('tests passed')
