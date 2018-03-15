from linkedlist import ListNode
from linkedlist import array_to_nodes
from linkedlist import nodes_to_array
from heapq import heappush, heappop


def merge_k_lists(lists):

    h = list()
    result_head = ListNode(None)
    curr = result_head

    for head in lists:
        if head:
            heappush(h, (head.val, head))

    while h:
        val, head = heappop(h)
        curr.next = head
        curr = curr.next
        if head.next:
            head = head.next
            heappush(h, (head.val, head))

    return result_head.next


def test(nums_list):
    lists = list()
    for nums in nums_list:
        lists.append(array_to_nodes(nums))

    return nodes_to_array(merge_k_lists(lists))

assert test([[], [1], [3], [2]]) == [1, 2, 3]
assert test([[5]]) == [5]
assert test([[1, 3, 5], [2, 4, 6]]) == [1, 2, 3, 4, 5, 6]
assert test([[1, 2, 3, 4, 5], [], []]) == [1, 2, 3, 4, 5]
print('All tests passed')
