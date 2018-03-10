# quicksort for

def quicksort(nums):
    if not nums:
        return
    l, r = 0, len(nums) - 1
    # might need to shuffel nums
    quicksort_helper(nums, l, r)

def quicksort_helper(nums, l, r):
    pivot = nums[r]
    if l >= r:
        return

    low, high = l, r - 1

    while low < high:
        if nums[low] < pivot:
            low += 1
        elif nums[high] >= pivot:
            high -= 1
        else:
            tmp = nums[low]
            nums[low] = nums[high]
            nums[high] = tmp

    # swap pivot to the pivot point
    if nums[low] > pivot:
        tmp = nums[low]
        nums[low] = nums[r]
        nums[r] = tmp

    quicksort_helper(nums, l, low - 1)
    quicksort_helper(nums, low + 1, r)

# quick sort inplace
nums = []
quicksort(nums)
assert nums == []

nums = [1]
quicksort(nums)
assert nums == [1]

nums = [2, 1]
quicksort(nums)
assert nums == [1, 2]

nums = [-3, 10, 7, 9, -11, 6, 5]
quicksort(nums)
assert nums == [-11, -3, 5, 6, 7, 9, 10]

nums = [-3, 10, -17, 7, 9, -11, 6, 5]
quicksort(nums)
assert nums == [-17, -11, -3, 5, 6, 7, 9, 10]

nums = [-3, 10, -17, 7, 7, 7, 7, 9, -11, 6, 5]
quicksort(nums)
assert nums == [-17, -11, -3, 5, 6, 7, 7, 7, 7, 9, 10]
print('All test cases passed')
