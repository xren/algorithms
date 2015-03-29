# algorithm to find the kth to last element of a singly linked list

from linklist import Node

def findKthToLast(node, k):
    fast = node
    slow = node
    length = 0

    while fast:
        length += 1
        fast = fast.next

    fast = node

    for i in xrange(0, k):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    return slow

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d


print findKthToLast(a, 1).value
