
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

def array_to_nodes(numbers):
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

def nodes_to_array(head):
    results = []
    while head:
        results.append(head.val)
        head = head.next
    return results
