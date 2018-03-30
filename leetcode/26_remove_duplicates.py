
def remove_duplicate(nums):
    if not nums:
        return 0
    idx = 0
    for val in nums:
        if val != nums[idx]:
            idx += 1
            nums[idx] = val
    return idx + 1


def test(nums):
    l = remove_duplicate(nums)
    return nums[:l]


assert test([1, 1, 1, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
assert test([]) == []
assert test([1, 2, 3]) == [1, 2, 3]
assert test([1, 1, 1]) == [1]
print('test passed')
