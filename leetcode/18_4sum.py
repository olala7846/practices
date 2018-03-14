
def four_sum(nums, target):
    nums.sort()
    results = []
    seen = set()

    def add_to_results(a, b, c, d):
        if (a, b, c, d) not in seen:
            seen.add((a, b, c, d))
            results.append([a, b, c, d])


    n = len(nums)
    for i in xrange(0, n-3):
        for j in xrange(i+1, n-2):
            k = j + 1
            l = len(nums) - 1

            while k < l:
                s = nums[i] + nums[j] + nums[k] + nums[l]
                if s == target:
                    add_to_results(nums[i], nums[j], nums[k], nums[l])
                    while k < l and nums[k+1] == nums[k]:
                        k += 1

                    while k < l and nums[l-1] == nums[l]:
                        l -= 1

                    k += 1
                    l -= 1
                elif s < target:
                    k += 1
                else:
                    l -= 1

    return results

assert four_sum([1, 1, 0, 0], 4) == []
assert four_sum([1, 1, 0, 0], 2) == [[0, 0, 1, 1]]
assert four_sum([2, -1, -1, 1, 0, 0], 0) == [[-1, -1, 0, 2], [-1, 0, 0, 1]]
assert four_sum([1,0,-1,0,-2,2], 0) == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print('All four_sum tests passed')

# 4 sum with early stopping

def n_sum(n, nums, target, current, results):
    if len(nums) < n:
        return

    # nums are assume to be sorted already
    if target < nums[0] * n or target > nums[-1] * n:
        return


    if n == 2:
        l = 0
        r = len(nums) - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                results.append(current + [nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
            elif s < target:
                l += 1
            else:
                r -= 1
    else:
        idx = 0
        for idx, val in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx-1]:
                idx += 1
                continue
            n_sum(n-1, nums[idx+1:], target - val, current + [val], results)
            idx += 1

def new_four_sum(nums, target):
    results = list()
    nums.sort()
    n_sum(4, nums, target, [], results)
    return results


assert new_four_sum([1, 1, 0, 0], 4) == []
assert new_four_sum([1, 1, 0, 0], 2) == [[0, 0, 1, 1]]
assert new_four_sum([2, -1, -1, 1, 0, 0], 0) == [[-1, -1, 0, 2], [-1, 0, 0, 1]]
assert new_four_sum([1,0,-1,0,-2,2], 0) == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

print('All new_four_sum tests passed')
