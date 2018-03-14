class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        s = ''
        head = self
        while head:
            s += '({}) -> '.format(head.val)
            head = head.next
        return s


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


def to_nodes(numbers):
    head = None
    tail = None
    for i in numbers:
        if tail:
            tail.next = ListNode(i)
            tail = tail.next
        else:
            head = ListNode(i)
            tail = head
    return head

def to_list(head):
    results = []
    while head:
        results.append(head.val)
        head = head.next
    return results

def test(nums, n):
    head = to_nodes(nums)
    result = remove_nth_from_end(head, n)
    return to_list(result)

assert test([1], 1) == []
assert test([1, 2, 3, 4], 1) == [1, 2, 3]
assert test([1, 2, 3, 4], 3) == [1, 3, 4]
assert test([1, 2, 3, 4], 4) == [2, 3, 4]
print('All tests passed')
