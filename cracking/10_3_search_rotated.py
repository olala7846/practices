

def search_rotated(x, nums):
    l = 0
    r = len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if x == nums[m]:
            return m
        elif x == nums[l]:
            return l
        elif x == nums[r]:
            return r

        # right half always increase
        if nums[m] < nums[r]:
            if nums[m] < x < nums[r]:
                l = m + 1
                r = r - 1
            else:
                r = m - 1
                l = l + 1
        # left half always increase
        else:
            if nums[l] < x < nums[m]:
                l = l + 1
                r = m - 1
            else:
                r = r - 1
                l = m + 1

    if l == r and nums[l] == x:
        return l
    else:
        return -1

array = [1, 2, 3, 5, 7, 8, 12, 13, 15, 17]
for i in xrange(10):
    # rotate by 1
    array = array[1:] + array[:1]
    idx =  search_rotated(12, array)
    assert array[idx] == 12

    idx =  search_rotated(1, array)
    assert array[idx] == 1

    idx =  search_rotated(17, array)
    assert array[idx] == 17

    idx =  search_rotated(18, array)
    assert idx == -1

    idx =  search_rotated(9, array)
    assert idx == -1

print('All test cases passed')
