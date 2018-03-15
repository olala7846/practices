from linkedlist import ListNode
from linkedlist import array_to_nodes
from linkedlist import nodes_to_array


def merge_two_lists(l1, l2):
    head = ListNode(None)
    current = head
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 is not None else l2

    return head.next


def test(l1, l2):
    head1 = array_to_nodes(l1)
    head2 = array_to_nodes(l2)
    result = merge_two_lists(head1, head2)
    return nodes_to_array(result)


assert test([], []) == []
assert test([], [1, 2, 3]) == [1, 2, 3]
assert test([1, 2, 3], []) == [1, 2, 3]
assert test([5], [1, 2, 3]) == [1, 2, 3, 5]
assert test([1, 2, 3], [5]) == [1, 2, 3, 5]
assert test([0], [1, 2, 3]) == [0, 1, 2, 3]
assert test([1, 2, 3], [0]) == [0, 1, 2, 3]
assert test([-3, 1, 5, 10], [2, 3, 7]) == [-3, 1, 2, 3, 5, 7, 10]
assert test([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
assert test([], []) == []

print('All tests passed')
