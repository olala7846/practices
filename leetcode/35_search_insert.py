
def search_insert(nums, target):
    l, r = 0, len(nums)-1
    while l <=r :
        m = (l + r) /2
        if nums[m] >= target:
            r = m - 1
        else:
            l = m + 1
    return l


assert search_insert([], 3) == 0
assert search_insert([1, 2, 3], 5) == 3
assert search_insert([1, 2, 3, 4], 3) == 2
assert search_insert([1, 3, 5, 6], 2) == 1
assert search_insert([1, 4, 5, 6], 2) == 1
assert search_insert([1, 3, 5, 6], 0) == 0
print('All tests passed')
