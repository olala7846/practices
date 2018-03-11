
def max_area(height):
    walls = []
    for idx, height in enumerate(height):
        walls.append((height, idx))
    walls.sort(reverse=True)

    max_area = 0
    l, r = walls[0][1], walls[0][1]
    max_l, max_r = l, r
    for height, idx in walls[1:]:
        if idx > r:
            r = idx
        elif idx < l:
            l = idx
        area = (r - l) * height
        if area > max_area:
             max_l = l
             max_r = r
             max_area = area

    return max_area

assert max_area([0, 1, 0, 0, 10, 0, 1, 8, 3, 1]) == 24
assert max_area([5, 1, 0, 0, 10, 0, 8, 3, 5]) == 40
assert max_area([1, 1]) == 1
print('All test cases passed')
