
def three_sum(nums):
    triplets = []
    nums.sort()
    for x_idx, x in enumerate(nums):
        if x_idx != 0 and nums[x_idx] == nums[x_idx-1]:
            continue

        y_idx = x_idx + 1
        z_idx = len(nums) - 1
        while y_idx < z_idx:
            y = nums[y_idx]
            z = nums[z_idx]
            s = x + y + z

            if s < 0:
                y_idx += 1
            elif s > 0:
                z_idx -= 1
            else:
                triplets.append([x, y, z])
                while y_idx < z_idx and nums[y_idx] == nums[y_idx + 1]:
                    y_idx += 1

                while y_idx < z_idx and nums[z_idx] == nums[z_idx - 1]:
                    z_idx -= 1
                y_idx += 1
                z_idx -= 1

    return triplets

print three_sum([-1, 0, 1, 2, -1, -4])
print('All test cases passed')
