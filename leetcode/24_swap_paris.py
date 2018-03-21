from linkedlist import ListNode
from linkedlist import array_to_nodes
from linkedlist import nodes_to_array

def swap_pairs(head):
    fake_head = ListNode(None)
    fake_head.next = head
    prev = fake_head
    while prev.next and prev.next.next:
        r1 = prev.next
        r2 = r1.next

        r1.next = r2.next
        prev.next = r2
        r2.next = r1
        prev = r

    return fake_head.next

def test(nums):
    head = array_to_nodes(nums)
    return nodes_to_array(swap_pairs(head))

assert test([1, 2, 3, 4, 5, 6]) == [2, 1, 4, 3, 6, 5]
assert test([6, 5]) == [5, 6]
assert test([]) == []
assert test([1, 2, 3]) == [2, 1, 3]
print('All test passed')
