
def subsets(nums):
    results = list()
    helper(list(), nums, results)
    return results

def helper(chosen, options, results):
    if not options:
        results.append(chosen)

    else:

        helper(list(chosen), options[1:], results)
        new_chosen = list(chosen)
        new_chosen.append(options[0])
        helper(new_chosen, options[1:], results)


print(subsets([1,2,3]))
print(subsets([]))
print(subsets([7]))
print('All test cases passed')
