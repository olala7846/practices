from collections import deque
from linkedlist import ListNode
from linkedlist import nodes_to_array
from linkedlist import array_to_nodes

def reverse_k_group(head, k):
    stack = deque()
    fake_head = ListNode(None)
    fake_head.next = head
    group_head = fake_head

    while True:
        has_group = True
        runner = group_head.next
        for i in xrange(k):
            if not runner:
                has_group = False
                break
            stack.append(runner)
            runner = runner.next

        if not has_group:
            return fake_head.next

        group_tail = runner
        next_head = group_head.next

        while stack:
            node = stack.pop()
            group_head.next = node
            group_head = group_head.next

        group_head.next = group_tail
        group_head = next_head

    return fake_head.next


def test(array, k):
    head = array_to_nodes(array)
    result = reverse_k_group(head, k)
    return nodes_to_array(result)

assert test([1, 2], 1) == [1, 2]
assert test([1, 2, 3], 2) == [2, 1, 3]
assert test([1, 2, 3, 4, 5], 2) == [2, 1, 4, 3, 5]
assert test([1, 2, 3, 4, 5, 6], 4) == [4, 3, 2, 1, 5, 6]
print('All tests passed')
