
def possible_ways(n):
    ways = [1, 1, 2]
    if n < 3:
        return ways[n]
    for i in range(3, n+1):
        num_ways = ways[i-1] + ways[i-2] + ways[i-3]
        ways.append(num_ways)

    return ways[n]


assert(possible_ways(0)) == 1
assert(possible_ways(1)) == 1
assert(possible_ways(2)) == 2
assert(possible_ways(3)) == 4
assert(possible_ways(4)) == 7
assert(possible_ways(5)) == 13
print('All test cases passed')
