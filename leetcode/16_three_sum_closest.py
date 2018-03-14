
def three_sum_closest(nums, target):
    nums.sort()
    min_dist = abs(nums[0] + nums[1] + nums[2])
    min_triplet = (nums[0], nums[1], nums[2])

    for i in xrange(len(nums)):
        j = i+1
        k = len(nums) - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            dist = abs(s - target)
            if dist < min_dist:
                min_dist = dist
                min_triplet = (nums[i], nums[j], nums[k])

            if s < target:
                j += 1
            elif s > target:
                k -= 1
            else:
                break

    return sum(min_triplet)

assert three_sum_closest([-1, 2, 1, -4], 1) == 2
assert three_sum_closest([0, 0, 0], 1) == 0

