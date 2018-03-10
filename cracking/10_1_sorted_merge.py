# merge two sorted array (assume nums1 as enough extra spaces)

def sorted_merge(nums1, nums2, len1, len2):
    idx1 = len1 - 1
    idx2 = len2 - 1
    if len2 == 0:
        return nums1
    to_update = len1 + len2 - 1
    while idx1 >= 0 and idx2 >= 0:
        if nums1[idx1] > nums2[idx2]:
            nums1[to_update] = nums1[idx1]
            idx1 -= 1
        else:
            nums1[to_update] = nums2[idx2]
            idx2 -= 1
        to_update -= 1

    while idx2 >= 0:
        nums1[to_update] = nums2[idx2]
        to_update -= 1
        idx2 -= 1
    return nums1

assert sorted_merge([1, 2, 3, None, None], [7, 9], 3, 2) == [1, 2, 3, 7, 9]
assert sorted_merge([1, 9, 10, None, None], [3, 11], 3, 2) == [1, 3, 9, 10, 11]
assert sorted_merge([None, None], [3, 11], 0, 2) == [3, 11]
assert sorted_merge([1, 10], [], 2, 0) == [1, 10]
assert sorted_merge([], [], 0, 0) == []
print('All test cases passed')
