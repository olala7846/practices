from linkedlist import ListNode
from linkedlist import array_to_nodes
from linkedlist import nodes_to_array

def remove_nth_from_end(head, n):
    fast = head
    slow = head
    for i in xrange(n):
        fast = fast.next

    if fast is None:
        return slow.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return head


def test(nums, n):
    head = array_to_nodes(nums)
    result = remove_nth_from_end(head, n)
    return nodes_to_array(result)

assert test([1], 1) == []
assert test([1, 2, 3, 4], 1) == [1, 2, 3]
assert test([1, 2, 3, 4], 3) == [1, 3, 4]
assert test([1, 2, 3, 4], 4) == [2, 3, 4]
print('All tests passed')
