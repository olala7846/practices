def binary_search(nums, target):
    # find the first index that nums[i] >= target
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r)/2
        if nums[m] >= target:
            r = m-1
        else:
            l = m+1

    return l


def search_range(nums, target):
    l = binary_search(nums, target)
    r = binary_search(nums, target+1)
    if l == r:
        return [-1, -1]

    return [l, r-1]


assert search_range([5, 7, 7, 8, 8], 8) == [3, 4]
assert search_range([5, 7, 7, 8, 8, 9], 8) == [3, 4]
assert search_range([5, 7, 7, 8, 8, 9], 5) == [0, 0]
assert search_range([5, 7, 7, 8, 8, 9], 3) == [-1, -1]
assert search_range([5, 7, 7, 8, 8, 9], 10) == [-1, -1]
assert search_range([], 10) == [-1, -1]
print('All test passed')
