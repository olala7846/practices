def search_in_range(nums, l, r, target):
    if l > r:
        return -1
    if nums[l] == target:
        return l
    if nums[r] == target:
        return r

    m = (l + r) / 2
    if nums[m] == target:
        return m

    if nums[l] < nums[m]:
        if nums[l] < target < nums[m]:
            return search_in_range(nums, l+1, m-1, target)
        else:
            return search_in_range(nums, m+1, r-1, target)
    else:
        if nums[m] < target < nums[r]:
            return search_in_range(nums, m+1, r-1, target)
        else:
            return search_in_range(nums, l+1, m-1, target)


def search(nums, target):
    l = 0
    r = len(nums) - 1
    return search_in_range(nums, l, r, target)


assert search([5, 6, 7, 1, 2, 3, 4], 5) == 0
assert search([5, 6, 7, 1, 2, 3, 4], 6) == 1
assert search([5, 6, 7, 1, 2, 3, 4], 7) == 2
assert search([5, 6, 7, 1, 2, 3, 4], 1) == 3
assert search([5, 6, 7, 1, 2, 3, 4], 2) == 4
assert search([5, 6, 7, 1, 2, 3, 4], 3) == 5
assert search([5, 6, 7, 1, 2, 3, 4], 4) == 6
assert search([5, 6, 7, 1, 2, 3, 4], 8) == -1
assert search([5, 6, 7, 1, 2, 3, 4], 0) == -1
assert search([1], 1) == 0
print('All test passed')
