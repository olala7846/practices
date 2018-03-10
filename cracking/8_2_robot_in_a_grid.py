from collections import deque

def can_move(r, c, obstacles):
    start = (0, 0)
    destination = (r-1, c-1)
    search = deque([start])
    explored = set()

    while search:
        x, y = search.popleft()
        if (x, y) == destination:
            return True  # found route

        move_right = (x+1, y)
        if (move_right[0] < r and
                move_right not in obstacles and
                move_right not in explored):
            search.append(move_right)
            explored.add(move_right)

        move_down = (x, y+1)
        if (move_down[1] < c and
                move_down not in obstacles and
                move_down not in explored):
            search.append(move_down)
            explored.add(move_down)

    return False  # not found


assert can_move(5, 4, set([(1, 0), (2, 2)]))
assert not can_move(5, 4, set([(1, 0), (0, 1)]))
print('All test cases passed')
