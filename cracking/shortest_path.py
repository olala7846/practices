# Dijkstra's algorithm for shortest path
# use a heap to find current nearest vertex with O(log E) time
from heapq import *


def dijkstra(graph, src, dest):

    visited = set()
    prev_dict = dict()

    min_heap = []
    # (cost, vertex, prev)
    heappush(min_heap, (0, src, src))
    while min_heap:
        cost, v, prev = heappop(min_heap)
        if v in visited:
            continue
        else:
            visited.add(v)
            prev_dict[v] = prev

        # construct shorted path
        if v == dest:
            path = [dest]
            while prev != src:
                path = [prev] + path
                prev = prev_dict[prev]
            return [src] + path
        else:
            for next_v, edge_cost in graph[v].iteritems():
                heappush(min_heap, (cost + edge_cost, next_v, v))

    return None

graph = {
  'A': {
    'B': 14,
    'C': 9,
    'D': 7,
  },
  'B': {
    'E': 9,
  },
  'C': {
    'B': 2,
    'F': 11,
  },
  'D': {
    'C': 11,
    'F': 15,
  },
  'F': {
    'E': 6
  }
}

assert dijkstra(graph, 'A', 'E') == ['A', 'C', 'B', 'E']
assert dijkstra(graph, 'D', 'E') == ['D', 'F', 'E']
print('All tests passed')
