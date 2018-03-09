"""
Leetcode 04 find median for two sorted arrys
"""

def find_median_sorted_arrays(nums1, nums2):
    if not nums1 and not nums2:
        raise ValueError('Two empty arrays')

    # make sure len(num1) <= len(nums2)
    if len(nums1) > len(nums2):
        tmp = nums1
        nums1 = nums2
        nums2 = tmp

    len1, len2 = len(nums1), len(nums2)
    half = (len1 + len2) // 2
    idx1, idx2 = 0, half
    l, r = 0, len1

    while l <= r:
        idx1 = (l + r) // 2
        idx2 = half - idx1

        # move right
        if idx1 < len1 and nums2[idx2-1] > nums1[idx1]:
            l = idx1 + 1
            continue
        # move left
        if idx1 > 0 and nums1[idx1-1] > nums2[idx2]:
            r = idx1 - 1
            continue

        # found
        break

    # may have error here!
    right_min = nums1[idx1] if idx1 < len1 else nums2[idx2]
    right_min = right_min if idx2 == len2 else min(right_min, nums2[idx2])

    left_max = nums1[idx1-1] if idx1 > 0 else nums2[idx2-1]
    left_max = left_max if idx2 == 0 else max(left_max, nums2[idx2-1])

    if (len1 + len2) % 2 == 0:
        return (left_max + right_min) / 2.0
    else:
        return right_min


func = find_median_sorted_arrays
assert func([], [1,2,3]) == 2
assert func([7], [1,2,3]) == 2.5
assert func([1, 5], [1,2,3]) == 2
assert func([1, 3], [2]) == 2
assert func([1], [2, 3]) == 2
print('All test cases passed')
