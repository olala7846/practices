class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return 'Node(%d)' % self.val


def add_two_numbers(l1, l2):
    head = Node(l1.val + l2.val % 10)
    tail = head
    carry = (l1.val + l2.val) // 10
    l1 = l1.next
    l2 = l2.next

    while l1 or l2 or carry > 0:
        s = l1.val if l1 else 0
        s = s + l2.val if l2 else s
        s = s + carry if carry > 0 else s
        tail.next = Node(s % 10)
        tail = tail.next
        carry = s // 10

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return head


def number_to_linked_list(num):
    if num == 0:
        return Node(0)

    head = Node(num % 10)
    tail = head
    num = num // 10

    while num > 0:
        tail.next = Node(num % 10)
        tail = tail.next
        num = num // 10
    return head

def show_val(l1):
    s = ''
    while l1:
        s += str(l1.val)
        l1 = l1.next
    print(s)

l1 = number_to_linked_list(342)
l2 = number_to_linked_list(465)

print l1, l2
show_val(l1)
show_val(l2)

l3 = add_two_numbers(l1, l2)
show_val(l3)

print('All test cases passed')

