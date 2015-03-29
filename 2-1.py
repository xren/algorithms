# Write code to remove duplicates from an unsorted linked list
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

from linklist import Node

def removeDup(node):
    if node is None or node.next is None:
        return node

    current = node
    runner = node

    while current:
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next

        current = current.next
        runner = current

    return node

a = Node('a')
b = Node('a')
c = Node('a')
d = Node('a')

a.next = b
b.next = c
c.next = d


removeDup(a)

a.printAll()
