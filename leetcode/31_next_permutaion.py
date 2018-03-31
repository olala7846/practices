
def swap(nums, idx1, idx2):
    tmp = nums[idx1]
    nums[idx1] = nums[idx2]
    nums[idx2] = tmp

def revert(nums, start, end):
    l = start
    r = end
    while l < r:
        swap(nums, l, r)
        l += 1
        r -= 1

def next_permutation(nums):
    if not nums:
        return nums

    n = len(nums)
    pivot_val = nums[-1]
    pivot_idx = n - 1
    for i in xrange(n-1, -1, -1):
        if nums[i] >= pivot_val:
            pivot_val = nums[i]
            pivot_idx = i
        else:
            break

    if pivot_idx > 0:
        # find the next large and swap
        for i in xrange(n-1, -1, -1):
            if nums[i] > nums[pivot_idx-1]:
                swap(nums, i, pivot_idx-1)
                break

    revert(nums, pivot_idx, n-1)


def test(nums, result):
    next_permutation(nums)
    return nums == result

assert test([4, 1, 2, 3], [4, 1, 3, 2])
assert test([1, 2, 3], [1, 3, 2])
assert test([3, 2, 1], [1, 2, 3])
assert test([1, 1, 5], [1, 5, 1])
assert test([1, 5, 1], [5, 1, 1])
assert test([1], [1])
assert test([], [])
assert test([1, 2, 3, 3], [1, 3, 2, 3])
print('All test passed')
